import json
import os

DATA_FILE = "budget_data.json"

class ExpenseManager:
    def __init__(self):
        self.expenses = {}
    
    def add_expense(self, name: str, amount: float):
        self.expenses[name] = amount
    
    def delete_expense(self, name: str):
        if name in self.expenses:
            del self.expenses[name]
            return True
        else:
            return False
    def total_spending(self) -> float:
        return sum(self.expenses.values())

    def view_expenses(self) -> dict:
        return self.expenses

class BudgetManager:
    def __init__(self):
        self.budget_goal = None
    
    def set_budget_goal(self, amount: float):
        self.budget_goal = amount

    def view_budget_goal(self, total_spending: float):
        if self.budget_goal is None:
            return "No budget goal set yet."

        progress = self.budget_goal - total_spending
        if progress > 0:
            return f"Congrats you are ${progress:.2f} under your budget goal!"
        elif progress == 0:
            return "Notice: You've reached your budget goal."
        else:
            return f"You've exceeded your budget goal by ${abs(progress):.2f}."
    
    def personalized_budget(self, total_spending: float):
        if self.budget_goal is None:
            return "No budget goal set yet."
        
        remaining_budget = self.budget_goal - total_spending

        if remaining_budget < 0:
            return (f"Current Total Spending: ${total_spending:.2f}\n"
                "You've exceeded your budget goal. Consider reducing expenses.")
        else:
            suggested_savings = round(remaining_budget * 0.1, 2)
            return (f"1. Current Total Spending: ${total_spending:.2f}\n"
                    f"2. Remaining Budget: ${remaining_budget:.2f}\n"
                    f"3. Suggested Savings:${suggested_savings:.2f}")

class BudgetApp:
    def __init__(self):
        self.expense_manager = ExpenseManager()
        self.budget_manager = BudgetManager()
        self.data_file = DATA_FILE
        self.load_data() # load saved data on startup

    def save_data(self):
        data = {
            "expenses": self.expense_manager.expenses,
            "budget_goal": self.budget_manager.budget_goal  
        }

        with open(self.data_file, "w") as f:
            json.dump(data, f)
        print("Data saved successfully.")

    def load_data(self):
        if not os.path.exists(self.data_file):
            # no saved data yet
            return
        with open(self.data_file, "r") as f:
            data = json.load(f)
            self.expense_manager.expenses = data.get("expenses", {})
            self.budget_manager.budget_goal = data.get("budget_goal", None)
        print("Data loaded successfully.")

    def autosave(method):
        def wrapper(self, *args, **kwargs):
            result = method(self, *args, **kwargs)
            self.save_data()
            return result
        return wrapper 
         
    @autosave
    def add_expense(self, name: str, amount: float):
        self.expense_manager.add_expense(name, amount)
    
    @autosave
    def delete_expense(self, name: str):
        self.expense_manager.delete_expense(name)

    @autosave
    def add_multiple_expenses(self, expense_list: list):
        self.expense_manager.add_multiple_expenses(expense_list)

    @autosave
    def set_budget_goal(self, amount: float):
        self.budget_manager.set_budget_goal(amount)

    def view_expenses(self):
        return self.expense_manager.view_expenses()

    def view_budget_goal(self):
        return self.budget_manager.view_budget_goal(self.expense_manager.total_spending())

    def personalized_budget(self):
        return self.budget_manager.personalized_budget(self.expense_manager.total_spending())
    
    def total_spending(self):
        return self.expense_manager.total_spending()
