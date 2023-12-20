import uuid
from datetime import datetime, timezone

class Expense:
    def __init__ (self, id, title, amount,created_at, updated_at):
        self.id = id
        self.title = title
        self.amount = amount
        self.created_at = created_at
        self.updated_at = updated_at

    def update(self,):
        print(f"{self.title} is updated in our expenses")
        print(f"{self.amount} is updated in our expenses")
        print(f"{self.updated_at} is updated in our expenses")

    def to_dict(self):
        pass


class ExpenseDatabase:
    def __init__ (self):
        self.expense = []


    def add_expense(self,expense):
        self.expense.append(expense)
        print(f"{expense} added successfully")
        return expense.id
        


    def remove_expense(self,expense_id):
        self.expense = [expense for expense in self.expense if expense.id != id]
        print(f"Expenses with{expense_id} has been removed")


    def get_expense_by_id (self, expense_id):
        expense = [expense for expense in self.expense if expense_id == id]
        if len(expense) == 0:
            return None
        return expense[0]



    def get_expense_by_title(self, expense_title):
        get_expense = [expense for expense in self.expense if expense_title == expense_title]
        if len(get_expense) == 0:
            return None
        return get_expense[0]


    def to_dict(self):
        pass  



if __name__ == "__main__":
    Expense_1 = Expense(id=4,title="spent",amount=1000,created_at="20NOV2022",updated_at="20NOV2023")

    edb = ExpenseDatabase()
    print(edb.expense)



    




