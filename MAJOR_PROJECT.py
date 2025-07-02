import datetime

def add_transaction():
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if date.strip() == "":
        date = datetime.date.today().isoformat()

    t_type = input("Enter type (Income/Expense): ").strip().capitalize()
    category = input("Enter category (e.g., Food, Rent, Salary): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    with open("finance.csv", "a") as file:
        file.write(f"{date},{t_type},{category},{amount},{description}\n")

    print("!!! Transaction added !!!")

def view_transactions():
    try:
        with open("finance.csv", "r") as file:
            print("\n--- All Transactions ---")
            print("Date       | Type    | Category   | Amount | Description")
            print("----------------------------------------------------------")
            for line in file:
                date, t_type, category, amount, desc = line.strip().split(",")
                print(f"{date} | {t_type:<7} | {category:<10} | ₹{amount:<6} | {desc}")
    except FileNotFoundError:
        print("No records found yet.")

def view_summary():
    income = 0
    expense = 0
    try:
        with open("finance.csv", "r") as file:
            for line in file:
                _, t_type, _, amount, _ = line.strip().split(",")
                amount = float(amount)
                if t_type == "Income":
                    income += amount
                elif t_type == "Expense":
                    expense += amount
        print(f"\nTotal Income: ₹{income}")
        print(f"Total Expenses: ₹{expense}")
        print(f"Current Balance: ₹{income - expense}")
    except FileNotFoundError:
        print("No transactions to summarize.")

def search_by_date():
    date = input("Enter date to search (YYYY-MM-DD): ")
    found = False
    try:
        with open("finance.csv", "r") as file:
            print("\n--- Transactions on", date, "---")
            for line in file:
                if line.startswith(date):
                    print(line.strip())
                    found = True
        if not found:
            print("No transactions on this date.")
    except FileNotFoundError:
        print("No records found.")

def menu():
    while True:
        print("\n====== DAILY FINANCE TRACKER ======")
        print("1. Add Transaction")
        print("2. View All Transactions")
        print("3. View Summary")
        print("4. Search by Date")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            search_by_date()
        elif choice == "5":
            print("Exiting... Your data is saved in finance_log.csv")
            break
        else:
            print("Invalid choice. Please try again.")
            
menu()
