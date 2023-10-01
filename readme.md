# Accounting Software Transaction Report Generator

This Python application allows you to generate monthly transaction reports for a specific account in an accounting software database. It uses PostgreSQL as the database backend.

## Getting Started

Follow these steps to set up and run the application:

### Prerequisites

- Python 3.x
- PostgreSQL database server
- `psycopg2` library for Python

### Installation

1. Clone the Git repository:

   ```bash
   git clone https://github.com/your-username/accounting-software.git
   cd accounting-software
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Database Setup

1. Make sure you have a PostgreSQL server installed and running.

2. Create a PostgreSQL database for the application, and update the database connection parameters in the `utils/db_sql.py` file:

   ```python
   db_params = {
       "host": "localhost",
       "database": "your_database_name",
       "user": "your_username",
       "password": "your_password",
   }
   ```

3. Run the application to create the necessary database table:

   ```bash
   python main.py
   ```

### Usage

1. To insert random data into the database for testing purposes, uncomment the relevant section in `main.py`:

   ```python
   # Uncomment the following line to insert random data into the database
   # random_data_input()
   ```

   Run the script to insert random data:

   ```bash
   python main.py
   ```

2. To generate a report for a specific account and date range, use the `generate_report` function in `accounts_report.py`. Example:

   ```python
   generate_report(
       db, account_number="98529295", start_date="2023-01-01", end_date="2023-12-31"
   )
   ```

3. Run the script to generate the report:

   ```bash
   python main.py
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Replace `"your-username"`, `"your_database_name"`, `"your_username"`, and `"your_password"` with your actual database credentials. You can also customize this `readme.md` file further based on your project's specific requirements.#   t r a n s a c t i o n s _ m o d e l 
 
 
