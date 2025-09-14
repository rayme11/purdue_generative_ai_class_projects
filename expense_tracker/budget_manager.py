import os
import csv

class BudgetManager:
    """
    Manages the monthly budget: set, save, load, and track against expenses.
    """
    def __init__(self, filename='data/budget.csv'):
        self.filename = filename
        self.budget = None
        self.load_budget()

    def load_budget(self):
        """
        Loads the budget from a CSV file. If not present, creates with $100.
        """
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['budget'])
                writer.writerow([100.00])
        with open(self.filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    self.budget = float(row['budget'])
                    break
                except (ValueError, KeyError):
                    continue
        if self.budget is None:
            self.budget = 100.00

    def save_budget(self):
        """
        Saves the current budget to the CSV file.
        """
        with open(self.filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['budget'])
            writer.writerow([self.budget])

    def set_budget(self):
        """
        Prompts user to set the monthly budget amount and saves it.
        """
        try:
            self.budget = float(input('Enter monthly budget amount: '))
            self.save_budget()
            print(f'Budget set to ${self.budget:.2f}')
        except ValueError:
            print('Invalid budget amount.')

    def track_budget(self, total_expenses):
        """
        Compares total expenses to the budget and displays status.
        Args:
            total_expenses (float): Total expenses recorded so far.
        """
        if self.budget is None:
            print('No budget set. Please set a budget first.')
            return
        print(f'Total expenses: ${total_expenses:.2f}')
        if total_expenses > self.budget:
            print('Warning: You have exceeded your budget!')
        else:
            print(f'You have ${self.budget - total_expenses:.2f} left for the month.')

    def remaining_balance(self, total_expenses):
        """
        Returns remaining balance after expenses.
        """
        if self.budget is None:
            return 0.0
        return self.budget - total_expenses
