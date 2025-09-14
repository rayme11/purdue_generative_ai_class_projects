import csv
import os
from expense_tracker.expense import Expense

class ExpenseManager:
    """
    Manages expense entries: add, view, save, load, and calculate totals.

    Args:
        filename (str): CSV file to save/load expenses.
    """
    def __init__(self, filename='expenses.csv'):
        self.filename = filename
        self.expenses = []
        self.load_expenses()

    def add_expense(self):
        """
        Prompts user for expense details and adds a new Expense to the list.
        """
        from datetime import datetime
        date_str = input('Enter date (YYYY-MM-DD): ')
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            print('Invalid date format.')
            return
        category = input('Enter category (e.g., Food, Travel): ')
        try:
            amount = float(input('Enter amount: '))
        except ValueError:
            print('Invalid amount.')
            return
        description = input('Enter description: ')
        expense = Expense(date_str, category, amount, description)
        self.expenses.append(expense)
        print('Expense added.')

    def view_expenses(self):
        """
        Displays all valid expenses in the list.
        """
        if not self.expenses:
            print('No expenses recorded.')
            return
        print('\nExpenses:')
        for exp in self.expenses:
            if exp.is_valid():
                print(f"{exp.date} | {exp.category} | ${exp.amount:.2f} | {exp.description}")
            else:
                print('Incomplete expense entry skipped.')

    def save_expenses(self):
        """
        Saves all expenses to a CSV file.
        """
        with open(self.filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['date', 'category', 'amount', 'description'])
            writer.writeheader()
            for exp in self.expenses:
                writer.writerow(exp.to_dict())
        print('Expenses saved to file.')

    def load_expenses(self):
        """
        Loads expenses from a CSV file into the list.
        """
        if not os.path.exists(self.filename):
            return
        with open(self.filename, 'r') as f:
            reader = csv.DictReader(f)
            self.expenses = []
            for row in reader:
                exp = Expense.from_dict(row)
                if exp:
                    self.expenses.append(exp)

    def total_expenses(self):
        """
        Calculates the total amount of all valid expenses.
        Returns:
            float: Total expenses amount.
        """
        return sum(exp.amount for exp in self.expenses if exp.is_valid())
