def generate_report(db, account_number: str, start_date: str, end_date: str):
    """
    this function generate report can be modified diffrently based on the requirement, for now i have just added the basic report where it can be seacrchedd by account number , and transection date
    """
    # Query to fetch transactions for the specified account and date range
    query = """
            SELECT EXTRACT(YEAR FROM created_at) AS year,
                EXTRACT(MONTH FROM created_at) AS month,
                SUM(debit_amount - credit_amount) AS balance
            FROM Transactions
            WHERE account_number = %s
            AND created_at BETWEEN %s AND %s
            GROUP BY year, month
            ORDER BY year, month
        """

    # Execute the query
    db.cur.execute(query, (account_number, start_date, end_date))

    # Fetch all rows
    monthly_transactions = db.cur.fetchall()

    # Generate and print the monthly report
    print(f"Account Transactions Report for Account ID: {account_number}")
    print(f"Date Range: {start_date} - {end_date}\n")

    print("{:<10} {:<10} {:<10}".format("Year", "Month", "Balance"))
    print("-" * 30)

    total_balance = 0  # Initialize the total balance

    for row in monthly_transactions:
        year, month, balance = row
        total_balance += balance  # Update the total balance
        print("{:<10} {:<10} {:<10.2f}".format(int(year), int(month), balance))

    print("-" * 30)
    print(f"Total Balance: {total_balance:.2f}")
