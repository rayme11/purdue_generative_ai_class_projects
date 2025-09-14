class Expense:
    """
    Represents a single expense entry.

    Args:
        date (str): Date of the expense in YYYY-MM-DD format.
        category (str): Category of the expense (e.g., Food, Travel).
        amount (float): Amount spent.
        description (str): Brief description of the expense.
    """
    def __init__(self, date, category, amount, description):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def is_valid(self):
        """
        Checks if the expense entry has all required fields.
        Returns:
            bool: True if valid, False otherwise.
        """
        return all([
            self.date,
            self.category,
            self.amount is not None,
            self.description
        ])

    def to_dict(self):
        """
        Converts the expense entry to a dictionary.
        Returns:
            dict: Dictionary representation of the expense.
        """
        return {
            'date': self.date,
            'category': self.category,
            'amount': self.amount,
            'description': self.description
        }

    @staticmethod
    def from_dict(data):
        """
        Creates an Expense object from a dictionary.
        Args:
            data (dict): Dictionary with keys 'date', 'category', 'amount', 'description'.
        Returns:
            Expense or None: Expense object if valid, else None.
        """
        try:
            amount = float(data['amount'])
            return Expense(data['date'], data['category'], amount, data['description'])
        except (ValueError, KeyError):
            return None
