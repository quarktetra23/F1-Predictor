# Formula 1 Grid Prediction

This repository provides a Python-based pipeline for fetching current Formula 1 data, storing it in CSV files, and using machine learning techniques to predict the outcomes of the Abu Dhabi Grand Prix. The data is fetched from the Ergast API and includes information about drivers, driver standings, and circuits. The repository also contains a Jupyter Notebook where various machine learning models are applied to predict driver performance at the Abu Dhabi GP.

## Repository Structure

- **data.py**: A Python script for fetching data from the Ergast API and saving it to CSV files. The script gathers the following data:
  - Current F1 driver information
  - Current F1 driver standings
  - Abu Dhabi circuit information
  - Placeholder for Abu Dhabi GP predictions
  
- **Modeling Notebook**: A Jupyter Notebook that applies several machine learning techniques to the data collected by the `data.py` script. The models used in the notebook include:
  - Random Forest
  - Gradient Boosting
  - Support Vector Regression (SVR)
  - Neural Network
  - K-Nearest Neighbors
  - Linear Regression
  
- **CSV Files**: CSV files containing the data fetched by `data.py` and used for modeling:
  - `current_drivers.csv`: Contains information about current F1 drivers.
  - `driver_standings.csv`: Contains current driver standings.
  - `abu_dhabi_circuit_info.csv`: Contains information about the Abu Dhabi circuit.
  - `abu_dhabi_predictions_placeholder.csv`: A placeholder CSV file where machine learning model predictions for the Abu Dhabi GP are stored.

## Installation & Setup

To use this repository, you will need Python installed on your machine. You can also use a virtual environment to manage dependencies.

### Step 1: Clone the Repository
First, clone this repository to your local machine:

git clone https://github.com/yourusername/formula-1-data-prediction.git
cd formula-1-data-prediction

Step 2: Install Dependencies

Install the required Python libraries using pip:

pip install -r requirements.txt

Here is a sample requirements.txt:

pandas==1.3.3
requests==2.26.0
scikit-learn==0.24.2
tensorflow==2.6.0

Step 3: Run data.py to Fetch Data

Run the data.py script to fetch the data from the Ergast API and store it in CSV files. This will generate the data files for further use in machine learning models.

python data.py

Step 4: Run the Jupyter Notebook for Modeling

Open the Jupyter Notebook and apply machine learning models to predict the Abu Dhabi GP results.

jupyter notebook

In the notebook, the data from the CSV files will be loaded, and various machine learning models will be applied to predict the driver standings for the Abu Dhabi Grand Prix.
Data Description

    Driver Data (current_drivers.csv):
        driver_id: Unique identifier for the driver.
        code: Driver code (e.g., "HAM" for Lewis Hamilton).
        number: Driver's permanent racing number.
        name: Full name of the driver.
        nationality: Nationality of the driver.

    Driver Standings (driver_standings.csv):
        driver_id: Unique identifier for the driver.
        position: Driver's current position in the standings.
        points: Total points accumulated by the driver.
        wins: Number of wins for the driver.
        constructor: Name of the constructor the driver is racing for.

    Circuit Data (abu_dhabi_circuit_info.csv):
        circuit_id: Unique identifier for the Abu Dhabi circuit.
        circuit_name: Name of the circuit.
        location: Locality of the circuit.
        country: Country where the circuit is located.
        lat: Latitude of the circuit.
        long: Longitude of the circuit.

    Prediction Placeholder (abu_dhabi_predictions_placeholder.csv):
        driver_id: Unique identifier for the driver.
        position: Driver's position in the prediction.
        points: Predicted points for the driver.
        wins: Predicted wins for the driver.
        constructor: Constructor name.
        predicted_position: Placeholder column for predicted position by the model.

Machine Learning Models

The following machine learning models are applied in the Jupyter Notebook for predicting the driver standings for the Abu Dhabi Grand Prix:

    Random Forest: An ensemble method based on decision trees.
    Gradient Boosting: A boosting technique that builds models sequentially to minimize errors.
    Support Vector Regression (SVR): A regression technique based on support vector machines.
    Neural Network: A deep learning model based on layers of nodes (neurons).
    K-Nearest Neighbors (KNN): A non-parametric method used for classification and regression.
    Linear Regression: A statistical method for modeling the relationship between variables.

Each model will be trained using the available data, and predictions will be generated for the upcoming Abu Dhabi GP.
