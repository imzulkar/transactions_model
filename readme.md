# Transaction Report

This is a Python project that demonstrates how to generate a report from a transaction table in PostgreSQL. The project includes the following files:

* `main.py`: This is the main script that runs the program.
* `accounts_report.py`: This module contains the function to generate the report.
* `utils.py`: This module contains the database connection and query functions.

To run the program, clone the repository and install the required dependencies:

```
git clone https://github.com/your-username/transaction-report.git
cd transaction-report
pip install psycopg2
```

Once the dependencies are installed, you can run the program using the following command:

```
python main.py
```

The program will generate a report of the total transactions for each month for the specified account number and date range. The report will be printed to the console.

**Example usage:**

```
python main.py --account-number 98529295 --start-date 2023-01-01 --end-date 2023-12-31
```

This will generate a report of the total transactions for each month for account number 98529295 for the period from 2023-01-01 to 2023-12-31.

**Database model:**

The transaction table in PostgreSQL has the following columns:

* `id`: The unique identifier for the transaction.
* `date`: The date of the transaction.
* `account_number`: The account number associated with the transaction.
* `description`: A brief description of the transaction.
* `debit_amount`: The amount debited from the account.
* `credit_amount`: The amount credited to the account.
* `reference`: A reference number for the transaction.
* `created_at`: The timestamp when the transaction was created.

**Cloning the repository:**

To clone the repository, use the following command:

```
git clone https://github.com/imzulkar/transactions_model.git
```

This will create a new directory called `transaction-report` in your current directory.