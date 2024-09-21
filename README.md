Functional Programming Quotes (FPQ) Project Setup
This README provides instructions for setting up the Functional Programming Quotes (FPQ) project, including database initialization.
Prerequisites

Python 3.7 or higher
PostgreSQL

Setup Instructions

Clone the repository
cd <project-directory>

Set up a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies
pip install -r requirements.txt

Set up the database

Open PostgreSQL and create a new database named 'fpq':
CREATE DATABASE fpq;

If you need to use a different database name or credentials, update the SQL_URI in config.py.


Set up environment variables
Create a .env file in the project root and add:
DATABASE_URL=postgresql://postgres:1234@localhost/fpq
Adjust the URL if your PostgreSQL setup is different.
Initialize the database

Open main.py
Uncomment these lines:
pythonCopy# init_database()
# init_tables_data()

Run the script:
python main.py

After successful execution, comment out these lines again to prevent accidental reinitialization.


Verify setup
You can now run queries against your database to verify that it has been properly initialized with data.

Running the Project
After setup, you can run your project as needed. Make sure to keep the database initialization lines commented out in main.py to avoid reinitializing the database on subsequent runs.
Troubleshooting

If you encounter any database connection issues, verify that your PostgreSQL server is running and that the credentials in SQL_URI are correct.
For any Python-related issues, ensure you're using the correct version of Python and that all dependencies are properly installed.

If you encounter any other issues, please refer to the project documentation or reach out to the project maintainers.