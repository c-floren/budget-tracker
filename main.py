from budget_tracker import BudgetApp

def print_menu():
    print("\n=== Budget Tracker Menu ===")
    print("1. Add an expense")
    print("2. View expenses")
    print("3. Set budget goal")
    print("4. View budget goal status")
    print("5. View personalized budget summary")
    print("6. Delete an expense")
    print("7. Quit")

def main():
    app = BudgetApp()

    while True:
        print_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            name = input("Enter expense name: ").strip()
            while True:
                try:
                    amount = float(input(f"Enter amount for '{name}': ").strip())
                    if amount <= 0:
                        print("Please enter a positive number.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            app.add_expense(name, amount)
            print(f"Added expense '{name}' with amount ${amount:.2f}.")

        elif choice == "2":
            expenses = app.view_expenses()
            if not expenses:
                print("No expenses recorded yet.")
            else:
                print("Expenses:")
                for exp_name, exp_amount in expenses.items():
                    print(f" - {exp_name}: ${exp_amount:.2f}")

        elif choice == "3":
            while True:
                try:
                    goal = float(input("Enter your budget goal amount: ").strip())
                    if goal < 0:
                        print("Please enter a non-negative number.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            app.set_budget_goal(goal)
            print(f"Budget goal set to ${goal:.2f}.")

        elif choice == "4":
            status = app.view_budget_goal()
            print(status)

        elif choice == "5":
            summary = app.personalized_budget()
            print(summary)
        
        elif choice == "6":
            name = input("Enter expense name: ").strip()
            if app.delete_expense(name):
                print(app.delete_expense(name))
                print(f"Deleted expense '{name}'.")
            else:
                print(app.delete_expense(name))
                print(f"Expense '{name}' not found.")

        elif choice == "7":
            print("Goodbye! Your data is saved.")
            break

        else:
            print("Invalid choice, please select a number between 1 and 6.")

if __name__ == "__main__":
    main()
