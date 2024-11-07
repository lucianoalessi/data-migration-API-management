import argparse
from database.db_connection_config import get_db_engine
from database.create_tables import create_tables
from etl.csv_to_db import load_and_validate_data


# Main program flow
def main():
    # Setting up argparse
    parser = argparse.ArgumentParser(description="Project execution options.")
    parser.add_argument("--mode", choices=["config", "migrate", "api", "backup", "restore"], required=True,
                        help="Execution mode: 'config' to start database configuration, 'migrate' to load data from CSV, 'api' to start the API server, 'backup' to create an AVRO backup, 'restore' to restore data from AVRO.")
    args = parser.parse_args()

    if args.mode == "config":
        # 1- Database connection
        get_db_engine()
        
        # 2- Create tables
        create_tables()

    elif args.mode == "migrate":
        # 3- Load data from CSV to the DB
        load_and_validate_data('data/hired_employees.csv', 'hired_employees')
        load_and_validate_data('data/departments.csv', 'departments')
        load_and_validate_data('data/jobs.csv', 'jobs')
        print("Migration completed.")



# Run the main program only if this is the main file
if __name__ == '__main__':
    main()
