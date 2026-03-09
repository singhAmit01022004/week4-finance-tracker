import sys
from expense import Expense
import file_handler
import reports

class FinanceTracker:
    def __init__(self):
        data = file_handler.load_expenses()
        self.expenses = [Expense(**d) for d in data]
        self.budget = 0.0

    def add_expense(self):
        date = input("Enter date (YYYY-MM-DD): ")
        if not Expense.validate_date(date):
            print("❌ Invalid date format!")
            return
        try:
            amount = float(input("Amount: "))
            cat = input("Category: ")
            desc = input("Description: ")
            self.expenses.append(Expense(date, amount, cat, desc))
            file_handler.save_expenses(self.expenses)
            print("✅ Added!")
        except ValueError: print("❌ Invalid amount!")

    def view_expenses(self, expense_list=None):
        list_to_show = expense_list if expense_list is not None else self.expenses
        print(f"\n{'Date':<12} | {'Amount':<10} | {'Category':<12} | {'Description'}")
        print("-" * 60)
        for e in list_to_show:
            print(f"{e.date:<12} | ${e.amount:<9.2f} | {e.category:<12} | {e.description}")

    def search_expenses(self):
        query = input("Search category or description: ").lower()
        results = [e for e in self.expenses if query in e.category.lower() or query in e.description.lower()]
        self.view_expenses(results)

    def generate_report(self):
        month = input("Enter Month (YYYY-MM): ")
        total = reports.get_monthly_total(self.expenses, month)
        print(f"\nTotal for {month}: ${total:.2f}")
        if self.budget > 0:
            status = "Under" if total <= self.budget else "OVER"
            print(f"Budget Status: {status} Budget (${self.budget:.2f})")

    def run(self):
        while True:
            print("\n1. Add | 2. View | 3. Search | 4. Report | 5. Category Chart | 6. Budget | 7. Export | 8. Backup | 0. Exit")
            choice = input("Choice: ")
            if choice == '1': self.add_expense()
            elif choice == '2': self.view_expenses()
            elif choice == '3': self.search_expenses()
            elif choice == '4': self.generate_report()
            elif choice == '5': 
                breakdown = reports.get_category_breakdown(self.expenses)
                reports.generate_text_chart(breakdown)
            elif choice == '6': 
                self.budget = float(input("Enter monthly budget: "))
            elif choice == '7': 
                file_handler.export_to_csv(self.expenses)
                print("✅ Exported to data/exports/")
            elif choice == '8': 
                if file_handler.create_backup(): print("✅ Backup created!")
            elif choice == '0': break

if __name__ == "__main__":
    tracker = FinanceTracker()
    tracker.run()