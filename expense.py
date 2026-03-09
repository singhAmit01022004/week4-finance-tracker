from datetime import datetime

class Expense:
    def __init__(self, date, amount, category, description):
        self.date = date
        self.amount = float(amount)
        self.category = category.title()
        self.description = description

    def to_dict(self):
        return {
            "date": self.date,
            "amount": self.amount,
            "category": self.category,
            "description": self.description
        }

    @staticmethod
    def validate_date(date_str):
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False