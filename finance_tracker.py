import pandas as pd
import os
from datetime import datetime

FILE_NAME = "finance_data.csv"

# Create file if not exists
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["Date", "Type", "Category", "Amount", "Note"])
    df.to_csv(FILE_NAME, index=False)

def add_transaction():
    t_type = input("Type (Income/Expense): ").capitalize()
    category = input("Category: ")
    amount = float(input("Amount: "))
    note = input("Note (optional): ")

    date = datetime.now().strftime("%Y-%m-%d")

    new_data = pd.DataFrame([{
        "Date": date,
        "Type": t_type,
        "Category": category,
        "Amount": amount,
        "Note": note
    }])

    df = pd.read_csv(FILE_NAME)
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(FILE_NAME, index=False)

    print("✅ Transaction added!")

def show_summary():
    df = pd.read_csv(FILE_NAME)

    income = df[df["Type"] == "Income"]["Amount"].sum()
    expense = df[df["Type"] == "Expense"]["Amount"].sum()
    balance = income - expense

    print("\n📊 Finance Summary")
    print("------------------")
    print(f"Total Income : ₹{income}")
    print(f"Total Expense: ₹{expense}")
    print(f"Balance      : ₹{balance}")

def show_transactions():
    df = pd.read_csv(FILE_NAME)
    print("\n📒 All Transactions")
    print(df)

def menu():
    while True:
        print("\n=== Finance Tracker ===")
        print("1. Add Transaction")
        print("2. Show Summary")
        print("3. Show Transactions")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            show_transactions()
        elif choice == "4":
            print("👋 Exiting... Bye!")
            break
        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    menu()
