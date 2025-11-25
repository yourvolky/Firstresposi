expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    expenses.append({"name": name, "amount": amount})
    print("Expense added!\n")

def view_expenses():
    if not expenses:
        print("No expenses added yet.\n")
        return
    
    print("\nYour Expenses:")
    for i, item in enumerate(expenses, 1):
        print(f"{i}. {item['name']} - ₹{item['amount']}")
    print("")

def total_spent():
    total = sum(item["amount"] for item in expenses)
    print(f"\nTotal Spent: ₹{total}\n")

def run():
    while True:
        print("===== Budget Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spent")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_spent()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid input, try again.\n")

run()
