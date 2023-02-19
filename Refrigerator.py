import Data_structure
import File_manager as FM
import Food
import datetime

def date_comparison(date1, date2):
    date1_value = (int(date1[:4])-2020) * 365 + (int(date1[5:7]) * 31) + (int(date1[8:10]))
    date2_value = (int(date2[:4])-2020) * 365 + (int(date2[5:7]) * 31) + (int(date2[8:10]))
    return date1_value - date2_value


class Refrigerator(Data_structure.Heap):

    #############################
    ##### File read / write #####
    #############################

    def __init__(self):
        super().__init__()

        items = list()
        for type,name,use_by_date,stock in (item.strip().split(',') for item in FM.File_manager.read_file("Refrigerator.txt")):
            if type == "ingredient":
                items.append(Food.Ingredient(name, use_by_date, stock))
            elif type == "dish":
                items.append(Food.Dish(name, use_by_date, stock))
            else:
                pass
        self.build_heap_by_date(items)

    def save_refrigerator(self):
        contents = list()
        for item in self.data[1:]:
            item_str = ",".join([item.type, item.name, item.use_by_date, str(item.stock)])
            contents.append(item_str)
        FM.File_manager.write_file("Refrigerator.txt", contents)

    ################
    ##### CRUD #####
    ################

    def ingredient_create(self, name, use_by_date, stock): # 새로운 Ingredient 추가
        self.insert_item_by_date(Food.Ingredient(name, use_by_date, stock))

    def ingredient_read_all(self):
        cnt = 1
        for item in self.data[1:]:
            print(f"{str(cnt)}. {item}")
            cnt += 1

    def ingredient_read_all_by_date(self):
        for item in self.get_sorted_by_date().data[1:]:
            print(item)

    def ingredient_update_name(self, idx, new_name):
        self.data[idx].update_name(new_name)

    def ingredient_update_use_by_date(self, idx, new_use_by_date):
        old_use_by_date = self.data[idx].use_by_date
        self.data[idx].update_use_by_date(new_use_by_date)
        # key 가 달라지므로, heap 속성 복구를 위해 수행
        if old_use_by_date < new_use_by_date:
            self.upHeap_by_date(idx)
        else:
            self.downHeap_by_date(idx)

    def ingredient_update_stock(self, idx, new_stock):
        self.data[idx].update_stock(new_stock)

    def ingredient_delete_idx(self, idx):
        return self.remove_idx_by_date(idx) # return 값 : 삭제된 값 / 인덱스 범위 초과시 None

    #########################################
    ########## Additional Features ##########
    #########################################

    def ingredient_passed_date(self):
        result = [item for item in self.data[1:] if item.use_by_date < str(datetime.date.today())]
        if result:
            return result
        return None

    def ingredient_near_date(self):
        result = [item for item in self.data[1:] if 0 <= date_comparison(item.use_by_date, str(datetime.date.today())) < 3]
        if result:
            return result
        return None

    def check_use_by_date(self):
        passed = self.ingredient_passed_date()
        near = self.ingredient_near_date()
        return passed, near

    ##### Recipe #####

    def reduce_stock(self, idx):
        if not self.data[idx].reduce_stock():
            self.remove_idx_by_date(idx)
            return False
        return True

    def kinds_of_items(self):
        kinds = set()
        for item in self.data[1:]:
            kinds.add(item.name)
        return kinds

    def check_condition(self, recipe):
        for item in recipe.ingredients:
            if item not in self.kinds_of_items():
                return False
        return True

    def make_dish(self, recipe):
        if not self.check_condition(recipe):
            return False
        for idx in range(1,len(self.data) - 1):
            item = self.data[idx]
            if item.name in recipe.ingredients:
                if not item.reduce_stock():
                    self.remove_idx_by_date(idx)

        if recipe.name in self.kinds_of_items():
            for item in self.data[1:]:
                if item.name == recipe.name:
                    item.stock += 1
        else:
            self.ingredient_create(recipe.name, str(datetime.date.today()), 1)
        return True


if __name__ == "__main__":
    main_refrigerator = Refrigerator()
    main_recipe_book = Food.Recipe_book()
    main_refrigerator.make_dish(main_recipe_book.data[0])