class Budget:
    def __init__(self, categories, budget, expenses=0.0):
        self.__categories = categories
        self.__budget = budget
        self.__expenses = expenses
    
    def get_categories(self):
        return self.__categories
    
    def get_budget(self):
        return self.__budget

    def set_categories(self, new_category):
        self.__categories = new_category

    def set_budget(self, new_budget):
        try:
            if new_budget > 0:
                self.__budget = new_budget
            else:
                print('a $0.00 or negative budget will not be created')
        except Exception as e:
            print(f'Error: {e}')
            print('Budget must be a positive number')

    def add_expense(self, expense):
        if expense > 0:
            if expense <= self.__budget:
                self.__budget -= expense
                self.__expenses += expense
                print(f'Expense of ${expense:.2f} recorded. Budget remaining: ${self.__budget:.2f}')
            else:
                print('Expense exceeds allocated budget. Please re-evaluate.')
        else:
            print('Invalid expense amount')

    def total_expenses(self):
        return self.__expenses
        

current_budget = Budget('Car', 1500)

print(f'Category: {current_budget.get_categories()}')
print(f'Budget: ${current_budget.get_budget():.2f}')

print('Expense: Loan Payment: $850')
current_budget.add_expense(850)

current_budget.add_expense(-1)


print('Expense: Insurance:$1000')
current_budget.add_expense(1000)

print(f'Total Posted Expenses: ${current_budget.total_expenses():.2f}')