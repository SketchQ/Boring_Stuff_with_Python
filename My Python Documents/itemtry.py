def i() :
    if shopping_cart:
        for item in shopping_cart:
            print("Adding " + item + " to your cart")
        print("your order is complete")
    else:
        print("You must select an item before proceeding. ")

shopping_cart = []

i()
