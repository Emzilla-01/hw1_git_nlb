def ask_menu_choices():
"""
prepared to requirements in a quick sketch before class version was finalized
I don't have the full class script for the menu, but this is mine ;)
"""
    selection_text="""1. Sandwich\n2. Burger\n3. Coffee\n4. Coke\n5. Exit"""
    selection_dict = {1: "Sandwich",
                      2: "Burger",
                      3: "Coffee",
                      4: "Coke",
                      5: "Checkout"}
    cart = list()
    input_loop_flag = False
    # validation_flag = False
    while not input_loop_flag:
        try:
            menu_input = int(input(selection_text))
            cur_selection = selection_dict.get(menu_input)
            
            validation_input = str(input(f"You selected {cur_selection}, is that right? enter y/n"))
            if validation_input[0].lower() == "y":
                if cur_selection == selection_dict.get(5):
                    print("Thank you for your order!")
                    return(cart)
                cart.append(cur_selection)
                print(f"{cur_selection} added to cart\ncart is now {cart}")
                continue
            else:
                continue
        except ValueError as e:
            print("please enter a number from the menu")
    return(cart)