import psycopg2


class Database:
    def __init__(self) -> None:
        # Database connection parameters
        db_params = {
            "host": "localhost",
            "database": "transaction_db_v1",
            "user": "postgres",
            "password": "7874",
        }

        # Establish a connection to the PostgreSQL database
        self.conn = psycopg2.connect(**db_params)

        # Create a cursor object to interact with the database
        self.cur = self.conn.cursor()
        print("Database connected successfully")

    def create_table(self):
        # create database transaction table
        db_query = """
            CREATE TABLE IF NOT EXISTS transactions (
            id SERIAL PRIMARY KEY,
            date DATE NOT NULL,
            account_number VARCHAR(50) NOT NULL,
            description VARCHAR(255) NOT NULL,
            debit_amount DECIMAL(15, 2) NOT NULL,
            credit_amount DECIMAL(15, 2) NOT NULL,
            reference VARCHAR(50),
            created_at timestamp DEFAULT NOW()
            )
            """

        # execute db query

        self.cur.execute(db_query)
        self.conn.commit()
        # self.cur.close()
        print("Table created successfully")
        return True

    def insert_data(self, data):
        # insert data into database
        db_query = "INSERT INTO transactions (date, account_number, description, debit_amount, credit_amount, reference) VALUES (%s, %s, %s, %s, %s, %s)"
        self.cur.execute(db_query, data)
        self.conn.commit()
        return True

    def get_data(self):
        # get data from database
        db_query = "SELECT * FROM transaction"
        self.cur.execute(db_query)
        return self.cur.fetchall()

    def close(self):
        # close cursor and connection
        self.cur.close()
        self.conn.close()
        return True
