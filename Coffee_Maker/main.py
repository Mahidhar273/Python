from Menu import MENU, resources

Choice = input("what would you like espresso/latte/cappuccino").lower()
Balance = 0
Available_water = resources['water']
Available_milk = resources['milk']
Available_coffee = resources['coffee']


def coins_process():
    key = True
    quarters = int(input("Enter the number of the quarters"))
    dimes = int(input("Enter the number of the dimes"))
    nickles = int(input("Enter the number of the nickles"))
    pennies = int(input("Enter the number of the pennies"))
    total_value = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    print(total_value)
    order_price = MENU[Choice]['cost']
    if order_price == total_value:
        print(f"Here is your {Choice}")
    elif total_value > order_price:
        remaining = total_value - order_price
        print(f"Thanks for the ordering {Choice}, here is ur balance {round(remaining,2)}")
    elif order_price > total_value:
        print("You poor idiot, didn't you learn mathematics in primary? stay away from me. You stink")
        key = False
    return key


def available_resources():
    key = True
    if MENU[Choice]['ingredients']['water'] <= Available_water and MENU[Choice]['ingredients']['coffee'] <= Available_coffee:
        if Choice != 'espresso' and MENU[Choice]['ingredients']['milk'] > Available_milk:
            key = False
    else:
        print("Sorry resources are not available, money is refunded")
        key = False
    return key


while Choice != 'off':
    if Choice == 'report':
        print(f"Available water is {Available_water}")
        print(f"Available milk is {Available_milk}")
        print(f"Available coffee is {Available_coffee}")
    if coins_process():
        if available_resources():
            if Choice != 'espresso':
                Available_milk -= MENU[Choice]['ingredients']['milk']
            Available_water -= MENU[Choice]['ingredients']['water']
            Available_coffee -= MENU[Choice]['ingredients']['coffee']

    Choice = input("what would you like espresso/latte/cappuccino").lower()




