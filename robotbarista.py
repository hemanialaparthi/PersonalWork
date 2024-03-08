# robot barista ~
# uses chatgpt to generate random orders so users can get inspiration for their order

x = input("Welcome to Summer Coffee Shop! I am Alex the robot and I will be serving you. What is your name?\n")

mood_waiter = input("What mood like your waiter to have: ")

menu = ["White Coffee", "Black Coffee", "Chai", "Milk Tea", "Crackers (combo with any drink)", "white bread + butter/jam"]
others = ["coffee", "tea", "biscuits", "combo", "frappuccino"]

while True:
    y = input(f"{x}! We are so glad to have you here. Would you like to look at our menu? ")

    if y.lower() == "yes":
        recieved_order = input(f"Of course! This is our menu: {menu}. Feel free to pick what you want. ")
    elif y.lower() == "no":
        others_order = input("Do you have something in mind that you would like to order?")
        if others_order in others:
            pending_order = print("Thank you for your order. Your waiter will be at your table shortly to provide you more details of the availability of your order.")
        else:
            print("Invalid item. Your waiter will be at your table shortly to assist you.")
    else:
        print("Wrong Input. Please try again.")
        exit()
