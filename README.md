# Personal Expense Tracker

## Overview
This is a simple command-line Personal Expense Tracker built in Python for the Purdue Generative AI class project. It helps users log daily expenses, categorize them, and track spending against a monthly budget. Expenses are saved to and loaded from a CSV file for future reference.

## Features
- Set and update monthly budget (stored in `data/budget.csv`)
- Add new expenses (date, category, amount, description)
- Guided date entry (year, month, day prompts)
- View all recorded expenses
- Track budget and remaining balance
- Prevent adding expenses if budget is exhausted
- Save expenses to a CSV file
- Load previous expenses from a CSV file
- Interactive, menu-driven interface

## File Structure
```
expense_tracker/
    app.py              # Main application entry point
    expense.py          # Expense class
    expense_manager.py  # ExpenseManager class
    budget_manager.py   # BudgetManager class

data/
    expenses.csv        # Sample expense data
    budget.csv          # Budget data (auto-created, updated as expenses are entered)
```

## How to Run
1. **Install Python 3** if you don't have it already.
2. Open a terminal and navigate to the project folder.
3. Install required libraries:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the main application:
    ```bash
    python -m expense_tracker.app
    ```
5. Use the interactive menu (with keyboard navigation) to:
    - Set or update your monthly budget
6. Use the interactive menu (with keyboard navigation via up/down arrows) powered by `simple-term-menu` to:
    - Set or update your monthly budget
    - Add expenses (date entry is guided)
    - View expenses
    - Track budget and remaining balance
    - Save your data
    - Exit
    - Add expenses (date entry is guided)
    - View expenses
## Notes
- Expenses are stored in `data/expenses.csv`. You can edit this file directly to add sample data.
- Budget is stored in `data/budget.csv` and is updated automatically as expenses are entered. You can manually edit this file if needed.
- You cannot add expenses if your budget is exhausted or if the expense exceeds the remaining budget.
- All code is organized using Object-Oriented Programming for maintainability.
- The menu uses keyboard navigation (up/down arrows) via the `simple-term-menu` library for a better user experience.
- If you see errors about system package management, use a virtual environment as described above.
- Expenses are stored in `data/expenses.csv`. You can edit this file directly to add sample data.
- Budget is stored in `data/budget.csv` and is updated automatically as expenses are entered.
## Features
- Set and update monthly budget (stored in `data/budget.csv`)
- Add new expenses (date, category, amount, description)
- Guided date entry (year, month, day prompts)
## Python Environment Setup & How to Run

### 1. Install Python 3
Make sure you have Python 3 installed. You can check with:
```bash
python3 --version
```
If you need to install it, visit https://www.python.org/downloads/ or use Homebrew:
```bash
brew install python3
```

### 2. Create and Activate a Virtual Environment (Recommended)
This keeps your project dependencies isolated and avoids system conflicts.
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Libraries
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python -m expense_tracker.app
```

### 5. Use the Interactive Menu
Navigate with your keyboard (up/down arrows) to:
- Set or update your monthly budget
- Add expenses (date entry is guided)
- View expenses
- Track budget and remaining balance
- Save your data
- Exit
```
