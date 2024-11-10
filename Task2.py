class Budget:
    def __init__(self, categories, budget):
        self.__categories = categories
        self.__budget = budget
    
    def get_categories(self):
        return self.__categories
    
    def get_budget(self):
        return self.__budget

    def set_categorie(self, new_category):
        self.__categories = new_category

    def set_budget(self, new_budget):
        try:
            if new_budget > 0:
                self.__budget = new_budget
            else:
                print('a $0.00 or negative budget will not be created')
        except Exception as e:
            print(f'Error: {e}')
#
# example
category = Budget("School", 15000)
print(category.get_categories())
print(category.get_budget())

category.set_budget('a')
