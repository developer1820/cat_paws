print("-" * 50)
print("Welcom to 'Paws and Cart'.")
print("-" * 50)

menu = ""
user_chosen_item = ""
total_price = 0
added_items = ""
removing_item = ""

print("Welcome to your shopping cart!!")
print()

while menu != "4":
    menu = input("Please enter sutaible option from menu below:\n\
                                1. Add an Item to your cart.\n\
                                2. Remove an Item from your cart.\n\
                                3. View total cost of your cart.\n\
                                4. Checkout.\n\
                                : ")

    if menu == "1":
        items = ""
        items += "Whiskas Cat Food 12 Pouches : £4.50,"
        items += "Gourmet Perle Cat Food 40 Pouches : £16.75,"
        items += "Felix cat food 12 Pouches : £5.00,"
        items += "Purina One Dry Cat Food Chicken & Wholegrain 800G : £5.00,"
        items += "Sheba Wet Cat Food Tuna & Cod in Gravy 6 Pouches : £2.00,"
        items += "Gourmet Gold Tinned Cat Food : £0.70,"
        items += "IAMS Vitality Cat Food : £4.50,"
        items += "Sheba Classics Soup Adult Wet Cat Food : £2.30,"

        list_of_items = items.split(",")
        print("Please select a product from below:")
        print()
        for item in list_of_items:
            print(item)
        print()
        user_chosen_item = \
            input("What item would you like to add in your cart?")
        index_of_user_chosen_item = items.find(user_chosen_item)
        index_of_comma_of_user_chosen_item = \
            items.find(",", index_of_user_chosen_item)
        extract_item_with_price = \
            items[index_of_user_chosen_item:index_of_comma_of_user_chosen_item+1]
        added_items = added_items + extract_item_with_price
        item_price = extract_item_with_price.split("£")[1].split(",")[0]
        numeric_item_price = float(item_price)
        total_price = float(total_price + numeric_item_price)
        print("-" * 50)
        print(f"{extract_item_with_price} is added into your cart.")
        print("-" * 50)

    elif menu == "2":
        print("Please select item from your cart below to remove")
        for each in added_items.split(","):
            print(each)
        shopping_iteam = \
            input("What item would you like to remove from your cart?")
        index_of_shopping_iteam = added_items.find(shopping_iteam)
        comma1 = added_items.find(",", index_of_shopping_iteam)
        removing_item = added_items[index_of_shopping_iteam: comma1+1]
        added_items = added_items.replace(removing_item, "")
        item_price = removing_item.split("£")[1].split(",")[0]
        numeric_item_price = float(item_price)
        total_price = total_price - numeric_item_price
        print("-" * 50)
        print(f"{shopping_iteam} has been removed from your cart")
        print("-" * 50)

    elif menu == "3":
        print("The total cost of your cart is £{:.2f}".format(total_price))

    elif menu == "4":
        print("Taking to you at Checkout")
        print("List of your added items")
        for each in added_items.split(","):
            print(each)
        print("The total cost of your cart is £{:.2f}".format(total_price))

    else:
        print("Please select valid option")
