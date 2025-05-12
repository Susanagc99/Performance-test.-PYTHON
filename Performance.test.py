
import time

print("\nPRODUCTS INVENTORY")

#empty dictionary to save products
inventory = {}

def add_products():
    #request 5 products initially and define a counter
    print("\nAdd at least 5 products to inventory:")
    added_p = 0
    while True:
        #loop to request product and validate errors
        while True:
            print(f"\n📦 NEW PRODUCT:\n")
            product = input("Name: ").strip().lower()
            if product in inventory: #make sure the product is not duplicated
                print("⚠️  This product already exists in inventory")
                other_p = input ("Would you like to add another producto? (yes/no): ")
                if other_p != "yes":
                    return
                else:
                    continue

            
            while True:
                #positive price validation and valid input
                try:
                    price = float(input("Price: "))
                    if price <0:
                        print("⚠️  Error! the number must be a positive number\n")
                    else:
                        break
                except ValueError:
                    print("⚠️  Invalid entry. Try again\n")
                
        
            while True:
                #positive units validation and valid input
                try:
                    units = int(input("Units#: "))
                    if units <0:
                        print("⚠️  Error! the number must be a positive number\n")
                    else:
                        break
                except ValueError:
                    print("⚠️  Invalid entry. Try again\n")
                    
            #add product to the dictionary with its attributes       
            inventory[product] = {"price":float(price),
                            "units": int(units)
                            }    
            
            #show product info and ensure it is saved in dictionary   
            print ("\nWe are saving the changes. Please wait...")        
            time.sleep(3)
            print (f"✅ The new product '{product}' was successfully saved")
            
            #add one by one the added products
            added_p += 1


            if added_p >= 5: #Until the first 5 are added, the options menu will not appear again.
                continuar = input("\nWould you like to add another product? (yes/no): ").lower().strip()
                if continuar != "yes":
                    options_menu() 


def serch_product():
    while True:
        #request product to search and display complete information
        view_p = input ("\nWhich product do you want to search for?:\n>> ").strip().lower()
        #verify that the product exists in inventory
        if view_p in inventory:
            product_info = inventory[view_p]
            print ("✅  Product found:")
            print (f"Name >> {view_p}")
            print (f"Price >> {product_info['price']}")
            print (f"Units available >> {product_info['units']}")
            break #the loop is broken because the requested product has already been found
            #if it does not exist, show the error and return to the initial question 
        else:
            print("⚠️  Producto not found. Try again")
    
        
        
def update_prices():
    print ("\n📃  The existing products are:")
    #displays inventory products to provide clarity to the user
    for exist in inventory:
        print(f">> {exist}")
    
    while True:
        #request product to be modified
        modify_p = input("\nWhich product do you want to modify?:\n>> ").strip().lower()
        #verify that the product exists in inventory
        if modify_p in inventory:
            while True:
                try:
                    #show current price before requesting a new one
                    current = inventory[modify_p]            
                    print(f"The current price of '{modify_p}' is ${current['price']}")
                    #request new price
                    new_price = float(input("Enter the new price: "))
                    if new_price <=0:
                        print("⚠️  Error! the number must be a positive number\n")
                        continue
                    inventory[modify_p]['price'] = new_price
                    print (f"✅  Successful update! The new price for '{modify_p}' is ${new_price}")
                    return #exit the entire function because the initial purpose has been achieved
                except ValueError:
                    print("⚠️  Invalid entry. Try again\n")
        else: #If it is not in the inventory, it prints an error and returns to the initial question.
            print("⚠️  This product doesn't exist. Try with another name\n")
                
                
            
def delete_product():
    print ("\n📃  The existing products are:")
    #displays inventory products to provide clarity to the user
    for exist in inventory:
        print(f">> {exist}")
        
    while True:
        rm_product = input("\nWhich product do you want to remove?:\n>> ").strip().lower()
        #verify that the product exists in inventory
        if rm_product in inventory:
            #confirm the existence of the product before removing it
            current = inventory[rm_product] 
            while True:
                print(f"\nThe product '{rm_product}' exists✅  and it has a price of ${current['price']} and there are {current['units']} units available")
                #confirm if the user wants to delete it
                confirmation = input("Are you sure you want to remove it? (yes/no): ").lower().strip()
                if confirmation == "yes":
                    del inventory[rm_product] #remove
                    print(f"✅  Successful update! You have removed the product '{rm_product}'")
                    return
                else: #If this is not the case, return to the main menu.
                    options_menu()
        else:
            print("⚠️  This product doesn't exist. Try with another name")
            continue           


def calculate_total():
    try:
        #display a nice and centered inventory summary
        print("\n"+"📦 Inventory summary".center(40))
        print("-" * 40)
        print(f"{'product'.ljust(15)} {'price'.rjust(10)} {'units'.rjust(10)}")
        print("-" * 40)
        
        #show summary of each product in the inventory
        for name, data in inventory.items(): #The items allow access to the product name and data.
            print(f"{name.ljust(15)} ${str(format(data['price'], '.2f')).rjust(10)} {str(data['units']).rjust(10)}")
        
        #get a list of values ​​per product with Lambda
        per_product = list (map(lambda prod: prod['price'] * prod ['units'], inventory.values()))

        #add the total values ​​per product from the created list
        total = sum(per_product)
        
        print(f"\n💰 The total value of the inventory is: ${total:.2f}")
    except Exception as e: #to prevent any possible errors
        print(f"⚠️ An error occurred while calculating inventory: {e}\n")
    
    
    
def options_menu():
    while True:
        #organized and pretty options menu :)
        print ("\n"+"OPTIONS MENU".center(40))
        print ("-"*40)
        print ("1. Add new products")
        print ("2. Serch for a product")
        print ("3. Update a product's price")
        print ("4. Remove a product from inventary ")
        print ("5. Calculate the total value from inventory")
        print ("6. Log out")
        print ("-"*40)

        #we call each of the functions depending on the selected option
        opcion = input(">> Choose an option (1-6): ")
        if opcion == "1":
            add_products()
        elif opcion in ["1","2","3","4","5"] and not inventory:
            #If the user chooses an option between 2 and 5, and the inventory is empty, an error occurs
            print ("⚠️  Error! You must first add products to your inventory to select this option")
        elif opcion == "2":
            serch_product()
        elif opcion == "3":
            update_prices()
        elif opcion == "4":
            delete_product()
        elif opcion == "5":
            calculate_total()
        elif opcion == "6":
            print("Goodbye. You're leaving the program... ")
            break
        else: #validate that the user enters an option within the range
            print("Invalid option. Try again")


options_menu()




