import Refrigerator
import Food

# User Interface
opening_str = """[Refrigerator CRUD]"""

choice_str = """\
*******************
[1] CREATE
[2] READ
[3] UPDATE
[4] DELETE
[5] Additional Features
[6] Exit
*******************

Enter the number : """

additional_str = """\
*******************
[1] Check Use by Date
[2] Food Consumption
[3] Cookable Dish
[4] Cook Dish
[5] Check Recipe
[6] New Recipe
[7] Return to main menu
*******************

Enter the number : """

division_str = "\n********************\n"

update_str = """\
*******************
[1] UPDATE name
[2] UPDATE use by date
[3] UPDATE stock
*******************

Enter the number : """

return_msg = "Returning to the main menu"
error_msg = "error : " + return_msg

print(f"\n{opening_str}\n")

main_refrigerator = Refrigerator.Refrigerator()
main_recipe_book = Food.Recipe_book()

while True:
    try:
        choice = (input(choice_str))
        choice = int(choice)
        print(division_str)
        print()

        if choice == 1:  # create - insert ingredient to the refrigerator
            name = input("name : ")
            use_by_date = input("use by date (YYYY-MM-DD) : ")
            stock = input("number of stock : ")
            main_refrigerator.ingredient_create(name, use_by_date, stock)

        elif choice == 2:  # show all items in refrigerator
            main_refrigerator.ingredient_read_all_by_date()

        elif choice == 3:  # update information of ingerdiens
            main_refrigerator.ingredient_read_all()
            idx = int(input("Enter the number to modify : "))
            update_op = int(input(update_str))
            if update_op == 1: # name update
                main_refrigerator.ingredient_update_name(idx, input(f"new name of ({main_refrigerator.data[idx]}): "))
            elif update_op == 2: # use by date update
                main_refrigerator.ingredient_update_use_by_date(idx, input(f"new use by date of ({main_refrigerator.data[idx]})(YYYY-MM-DD) : "))
            elif update_op == 3: # stock update
                main_refrigerator.ingredient_update_stock(idx, int(input(f"new stock of ({main_refrigerator.data[idx]}) : ")))
            else:
                print(error_msg)


        elif choice == 4:  # delete a specific ingredient
            main_refrigerator.ingredient_read_all()
            idx = int(input("Enter the number to delete : "))
            removed = main_refrigerator.ingredient_delete_idx(idx)
            if removed:
                print(f"{removed} deleted")
            else:
                print(error_msg)


        elif choice == 5: # Adittional
            choice = int(input(additional_str))
            print()
            if choice == 1: # check use by date
                passed, near = main_refrigerator.check_use_by_date()
                if passed:
                    print("***** Expired *****")
                    for item in passed:
                        print(item)
                if near:
                    print("***** near date *****")
                    for item in near:
                        print(item)
                if (not passed) & (not near):
                    print("all items has enough time.")

            elif choice == 2: # Food consumption
                print()
                main_refrigerator.ingredient_read_all()
                idx = int(input("Enter the number to consume: "))
                consumption = int(input("consumption : "))
                temp_name = main_refrigerator.data[idx].name
                if consumption > main_refrigerator.data[idx].stock:
                    print("not enough stock")
                    print(return_msg)
                for i in range(consumption):
                    if not main_refrigerator.reduce_stock(idx):
                        print(f"all {temp_name} consumed")
                input()


            elif choice == 3: # Cookable Dish
                flag = False
                for recipe in main_recipe_book.data:
                    if main_refrigerator.check_condition(recipe):
                        print(recipe)
                        flag = True
                if not flag:
                    print("nothing available")

            elif choice == 4: # Cook Dish
                print(main_recipe_book.print_all_recipe())
                if not main_refrigerator.make_dish(main_recipe_book.data[int(input("choose a number : ")) - 1]):
                    print("insufficient ingredients")

            elif choice == 5: # Check Recipe
                main_recipe_book.print_all_recipe()

            elif choice == 6: # New Recipe
                name = input("Dish name : ")
                ingredients = list()
                ingredients_cnt = int(input("number of ingredients (int) : "))
                for i in range(ingredients_cnt):
                    ingredients.append(input(f"ingredient{i+1} : "))
                main_recipe_book.create_recipe(name, ingredients)

            elif choice == 7: # Return to Main Menu
                print(return_msg)

            else:
                print(error_msg)

        elif choice == 6:
            main_refrigerator.save_refrigerator()
            main_recipe_book.save_recipe()
            print("file saved")
            print("exit program")
            break

        else:
            print(error_msg)

        input() # 입력 대기 : 바로 메인화면으로 넘어가는것을 방지.
    except:
        print(error_msg)
        if choice == "exit":
            break