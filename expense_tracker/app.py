from expense_tracker.expense_manager import ExpenseManager
from expense_tracker.budget_manager import BudgetManager
from simple_term_menu import TerminalMenu

class ExpenseTrackerApp:
    """
    Main application class for the Personal Expense Tracker.
    Coordinates expense and budget management, and provides the menu interface.
    """
    def __init__(self):
        self.expense_manager = ExpenseManager()
        self.budget_manager = BudgetManager()

    def menu(self):
        """
        Displays the interactive menu and handles user choices.
        Only accepts integer options from 1 to 6.
        """
        while True:
            options = [
                "0 - Set monthly budget (update budget.csv)",
                "1 - Add expense (deducts from budget, updates expenses.csv and budget.csv)",
                "2 - View expenses (shows all recorded expenses)",
                "3 - Track budget (shows total spent and remaining balance)",
                "4 - Save expenses manually (writes current expenses to expenses.csv)",
                "5 - Exit (saves expenses and exits)"
            ]
            terminal_menu = TerminalMenu(options, title="\n=== Personal Expense Tracker ===")
            menu_entry_index = terminal_menu.show()
            total = self.expense_manager.total_expenses()
            if menu_entry_index == 0:
                self.budget_manager.set_budget()
            elif menu_entry_index == 1:
                remaining = self.budget_manager.remaining_balance(total)
                if remaining <= 0:
                    print(f'Insufficient balance. You cannot add more expenses. Budget exhausted.')
                else:
                    print(f'Remaining balance: ${remaining:.2f}')
                    from datetime import datetime
                    print('Enter date:')
                    year = input('  Year (YYYY): ')
                    if not (year.isdigit() and len(year) == 4):
                        print('Invalid year format.')
                        continue
                    month = input('  Month (MM): ')
                    if not (month.isdigit() and len(month) == 2 and 1 <= int(month) <= 12):
                        print('Invalid month format.')
                        continue
                    day = input('  Day (DD): ')
                    if not (day.isdigit() and len(day) == 2 and 1 <= int(day) <= 31):
                        print('Invalid day format.')
                        continue
                    date_str = f"{year}-{month}-{day}"
                    try:
                        datetime.strptime(date_str, '%Y-%m-%d')
                    except ValueError:
                        print('Invalid date.')
                        continue
                    category = input('Enter category (e.g., Food, Travel): ').strip()
                    if not category:
                        category = input('Category is required. Please enter a category: ').strip()
                        if not category:
                            print('No category entered. Cancelling expense entry and returning to main menu.')
                            continue
                    try:
                        amount = float(input('Enter amount: '))
                    except ValueError:
                        print('Invalid amount.')
                        continue
                    if amount > remaining:
                        print(f'Insufficient balance. You can only spend up to ${remaining:.2f}.')
                        continue
                    description = input('Enter description: ').strip()
                    if not description:
                        description = input('Description is required. Please enter a description: ').strip()
                        if not description:
                            print('No description entered. Cancelling expense entry and returning to main menu.')
                            continue
                    from expense_tracker.expense import Expense
                    expense = Expense(date_str, category, amount, description)
                    self.expense_manager.expenses.append(expense)
                    self.budget_manager.budget -= amount
                    self.budget_manager.save_budget()
                    print(f'Expense added. New remaining balance: ${self.budget_manager.budget - self.expense_manager.total_expenses():.2f}')
            elif menu_entry_index == 2:
                self.expense_manager.view_expenses()
            elif menu_entry_index == 3:
                self.budget_manager.track_budget(total)
            elif menu_entry_index == 4:
                self.expense_manager.save_expenses()
            elif menu_entry_index == 5:
                self.expense_manager.save_expenses()
                print('Goodbye!')
                break

if __name__ == '__main__':
    """
    Entry point for running the Personal Expense Tracker application.
    """
    app = ExpenseTrackerApp()
    app.menu()
