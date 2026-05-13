def main():
    inventory = {}
    while True:
        print("\n----MENU----")
        print("1. Add Product")
        print("2. check Stock")
        print("3.Check Low Stock (< 5) ")
        print("4. Exit")
        choice = input("enter your choice:")

        if choice == "1":
            name = input("enter product name:")
            quantity = int(input("enter quantity:"))
            inventory[name] = quantity
            print("Successfully added to stock.")
            
        elif choice == "2":
            print("----Current Stock----")
            if not inventory:
                print("No products in inventory.")
            else:
                for name, quantity in inventory.items():
                    print(f"{name}: {quantity}")
        elif choice == "3":
            print("----Low stock Products (<5)----")
            found_low = False
            for name, quantity in inventory.items():
                if quantity < 5:
                    print(f"WARNING: {name} has low stock ({quantity} units left)")
                    found_low = True

            if not found_low:
             print("All products have sufficient stock.")
        elif choice == "4":
            print("exiting program!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":   
    main()          



    