#6/9/25

"""
Design a Grocery Management System . You can view the item list. add item. Delete Item. Clear List with the help of list in Python
"""

grocery_list = []

def display_items():
    if not grocery_list:
        print("The grocery list is empty.")
    else:
        print("Grocery List:")
        for index, item in enumerate(grocery_list):
            print(f"{index + 1}. {item}")

def add_item(item):
    grocery_list.append(item)
    print(f"'{item}' has been added to the grocery list.")

def delete_item(item):
    if item in grocery_list:
        grocery_list.remove(item)
        print(f"'{item}' has been removed")
    else:
        print(f"'{item}' is not in list")

def clear_list():
    grocery_list.clear()
    print("The grocery list has been cleared.")

def main():
    while True:
        print("\nGrocery Management System")
        print("1. View Items")
        print("2. Add Item")
        print("3. Delete Item")
        print("4. Clear List")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")


        match choice:
            case '1':
                display_items()
            case '2':
                item = input("Enter the item to add: ").lower()
                add_item(item)
            case '3':
                item = input("Enter the item to delete: ").lower()
                delete_item(item)
            case '4':
                clear_list()
            case '5':
                print("Exiting GMS")
                break
            case _:
                print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()