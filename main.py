from utils import db_sql
from accounts_report import generate_report
from random import randint


def random_data_input():
    # insert data into database
    account_number = str(randint(10000000, 99999999))
    print(account_number)
    for i in range(randint(100, 999)):
        amount = randint(0, 10000)
        debit_amount = amount if amount % 2 == 0 else 0
        credit_amount = amount if amount % 2 != 0 else 0

        date = f"{randint(2010,2023)}-{randint(1,12)}-{randint(1,28)}"
        data = (
            date,
            account_number,
            "Test Description",
            debit_amount,
            credit_amount,
            "Test Reference",
        )
        db.insert_data(data)


if __name__ == "__main__":
    # create db object
    db = db_sql.Database()

    db.create_table()  # create table if not exists

    # random value input
    # for i in range(100):
    #     random_data_input()

    generate_report(
        db, account_number="98529295", start_date="2023-01-01", end_date="2023-12-31"
    )
