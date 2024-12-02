import requests
import pandas as pd

# Base URL for Ergast API
BASE_URL = "http://ergast.com/api/f1"

# Function to fetch current drivers
def fetch_current_drivers():
    url = f"{BASE_URL}/current/drivers.json"
    response = requests.get(url)
    if response.status_code == 200:
        drivers = response.json()['MRData']['DriverTable']['Drivers']
        return pd.DataFrame([{
            "driver_id": driver['driverId'],
            "code": driver.get('code', None),
            "number": driver.get('permanentNumber', None),
            "name": f"{driver['givenName']} {driver['familyName']}",
            "nationality": driver['nationality']
        } for driver in drivers])
    else:
        print("Error fetching current drivers")
        return None

# Function to fetch driver standings
def fetch_driver_standings():
    url = f"{BASE_URL}/current/driverStandings.json"
    response = requests.get(url)
    if response.status_code == 200:
        standings = response.json()['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
        return pd.DataFrame([{
            "driver_id": driver['Driver']['driverId'],
            "position": int(driver['position']),
            "points": float(driver['points']),
            "wins": int(driver['wins']),
            "constructor": driver['Constructors'][0]['name']
        } for driver in standings])
    else:
        print("Error fetching driver standings")
        return None

def search_circuit_by_name(circuit_name):
    url = f"{BASE_URL}/circuits.json"
    response = requests.get(url)
    if response.status_code == 200:
        circuits = response.json()['MRData']['CircuitTable']['Circuits']
        for circuit in circuits:
            if circuit_name.lower() in circuit['circuitName'].lower():
                return circuit
        print(f"Circuit '{circuit_name}' not found.")
        return None
    else:
        print(f"Error fetching circuits: {response.status_code}")
        return None

# Example usage
circuit = search_circuit_by_name("Abu Dhabi")
if circuit:
    print(circuit)

# Function to fetch Abu Dhabi circuit information
def fetch_abu_dhabi_circuit_data():
    url = f"{BASE_URL}/circuits/abu_dhabi.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['MRData']['CircuitTable']['Circuits']:
            circuit_data = data['MRData']['CircuitTable']['Circuits'][0]
            return {
                "circuit_id": circuit_data['circuitId'],
                "circuit_name": circuit_data['circuitName'],
                "location": circuit_data['Location']['locality'],
                "country": circuit_data['Location']['country'],
                "lat": circuit_data['Location']['lat'],
                "long": circuit_data['Location']['long']
            }
        else:
            print("No circuit data found for Abu Dhabi.")
            return None
    else:
        print(f"Error fetching Abu Dhabi circuit data: {response.status_code}")
        return None


# Main execution
if __name__ == "__main__":
    # Fetch current drivers
    print("Fetching current drivers...")
    drivers_df = fetch_current_drivers()
    if drivers_df is not None:
        drivers_df.to_csv("current_drivers.csv", index=False)
        print("Saved current drivers to 'current_drivers.csv'")

    # Fetch driver standings
    print("\nFetching driver standings...")
    standings_df = fetch_driver_standings()
    if standings_df is not None:
        standings_df.to_csv("driver_standings.csv", index=False)
        print("Saved driver standings to 'driver_standings.csv'")

    # Fetch Abu Dhabi circuit data
    print("\nFetching Abu Dhabi circuit data...")
    abu_dhabi_data = fetch_abu_dhabi_circuit_data()
    if abu_dhabi_data is not None:
        abu_dhabi_df = pd.DataFrame([abu_dhabi_data])
        abu_dhabi_df.to_csv("abu_dhabi_circuit_info.csv", index=False)
        print("Saved Abu Dhabi circuit info to 'abu_dhabi_circuit_info.csv'")

    # Create placeholder for Abu Dhabi GP predictions
    print("\nCreating placeholder for predictions...")
    if drivers_df is not None and standings_df is not None:
        merged_df = pd.merge(drivers_df, standings_df, on="driver_id", how="inner")
        merged_df['predicted_position'] = None  # Placeholder for predictions
        merged_df.to_csv("abu_dhabi_predictions_placeholder.csv", index=False)
        print("Saved placeholder for predictions to 'abu_dhabi_predictions_placeholder.csv'")
