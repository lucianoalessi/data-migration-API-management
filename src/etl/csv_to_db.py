import os
import pandas as pd
from database.db_connection_config import get_db_engine

# Database connection
engine = get_db_engine()

# Function to validate and load data
def load_and_validate_data(file_path, table_name):
    try:
        df = pd.read_csv(file_path)
        
        # Validation that all fields are mandatory
        invalid_records = df[df.isnull().any(axis=1)]
        valid_records = df.dropna()
        
        # Log transactions that do not meet the rules
        if not invalid_records.empty:
            os.makedirs('data', exist_ok=True)  # Create the 'data' directory if it does not exist
            invalid_records.to_csv('data/invalid_records.csv', mode='a', header=False, index=False)
            print(f"{len(invalid_records)} invalid records have been logged in 'data/invalid_records.csv'.")

        # Load valid data into the database
        valid_records.to_sql(table_name, engine, if_exists='append', index=False)
        print(f"Data successfully loaded into the table '{table_name}'.")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"Error loading data into the table '{table_name}': {e}")
        

# Carga de archivos CSV
# if __name__ == '__main__':
#     load_and_validate_data('data/hired_employees.csv', 'hired_employees')
#     load_and_validate_data('data/departments.csv', 'departments')
#     load_and_validate_data('data/jobs.csv', 'jobs')