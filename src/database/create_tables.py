from database.db_connection_config import get_db_engine
from sqlalchemy import Table, Column, Integer, String, MetaData

# Database connection
engine = get_db_engine()

# Define a function for table creation
def create_tables():
    # Define the tables
    metadata = MetaData()

    hired_employees = Table('hired_employees', metadata,
                            Column('id', Integer, primary_key=True),
                            Column('name', String),
                            Column('datetime', String),
                            Column('department_id', Integer),
                            Column('job_id', Integer))

    departments = Table('departments', metadata,
                        Column('id', Integer, primary_key=True),
                        Column('department', String))

    jobs = Table('jobs', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('job', String))

    # Create the tables in the database
    metadata.create_all(engine)