import File_manager as FM

class Food:
    def __init__(self, name, use_by_date, stock):
        self.name = name
        self.use_by_date = use_by_date
        self.stock = int(stock)

    def update_name(self, new_name):
        self.name = new_name

    def update_use_by_date(self, new_use_by_date):
        self.use_by_date = new_use_by_date

    def update_stock(self, new_stock):
        self.stock = new_stock

    def reduce_stock(self):
        self.stock -= 1
        if self.stock == 0:
            return False # 재고가 다 떨어져 자동으로 삭제될 경우 False
        return True # 재고가 남았을 경우 True

    def get_date(self):
        return self.use_by_date

    # def get_name(self):
    #     return self.name

    def __str__(self): # print(Ingredient)
        return f"{self.name:<6} : {self.use_by_date} ({self.stock:>2})"

class Ingredient(Food):
    type = "ingredient"

class Dish(Food):
    type = "dish"

class Recipe_book:

    class recipe:
        def __init__(self, name, ingredients):
            self.name = name
            self.ingredients = ingredients # ingredients : 요리에 사용되는 식재료(Ingredient)를 포함하는 list

        def __str__(self):
            return f"{self.name:<10} : {', '.join(self.ingredients)}"

    def __init__(self):
        self.data = list()

        for line in FM.File_manager.read_file("Recipe.txt"):
            if len(line) < 3:
                continue
            name, ingredients = line.strip().split('/')
            ingredients = ingredients.split(',')
            self.data.append(self.recipe(name, ingredients))

    def create_recipe(self, name, ingredients):
        self.data.append(self.recipe(name, ingredients))

    def save_recipe(self):
        contents = list()
        for item in self.data:
            item_str = item.name + "/" + ",".join(item.ingredients)
            contents.append(item_str)
        FM.File_manager.write_file("Recipe.txt", contents)

    def print_all_recipe(self):
        for i in range(len(self.data)):
            print(f"{i+1}. {self.data[i]}")


# if __name__ == "__main__":
#     new_recipe_book = Recipe_book()
#     new_recipe_book.print_all_recipe()