

def display_menu(menu):
    print("Menu:")
    for item, price in menu.items():
        print(f"- {item}: ${price:.2f}")

def add_to_cart(cart, item, quantity, menu):
    if item in menu:
        cart[item] = cart.get(item, 0) + quantity
        print(f"{quantity} {item}(s) added to cart.")
    else:
        print("Invalid item.")

def view_cart(cart, menu):
     if not cart:
        print("Your cart is empty.")
        return
     print("Cart:")
     total_cost = 0
     for item, quantity in cart.items():
        price = menu[item]
        item_total = price * quantity
        print(f"- {item}: {quantity} x ${price:.2f} = ${item_total:.2f}")
        total_cost += item_total
     print(f"Total cost: ${total_cost:.2f}")

def remove_from_cart(cart, item, quantity):
    if item in cart:
        if cart[item] > quantity:
            cart[item] -= quantity
            print(f"{quantity} {item}(s) removed from cart.")
        elif cart[item] == quantity:
            del cart[item]
            print(f"{item} removed from cart.")
        else:
            print(f"Not enough {item}(s) in cart to remove.")
    else:
        print(f"{item} is not in your cart.")
        
def main():
    menu = {"apples": 1.0, "banana": 0.5, "oranges": 0.25, "grape": 2.0, "Brocoli": 1.25, "Onion": 0.15, "eggs": 0.75, "bell peper": 0.35, "watermelon": 5.0 }
    cart = {}
    while True:
        print("\nOptions: add | remove | total | menu | Quit")
        option = input("Choose an action: ").lower()

        if option == "add":
            display_menu(menu)
            item = input("Enter item to add: ").lower()
            quantity = int(input("Enter quantity: "))
            add_to_cart(cart, item, quantity, menu)
        elif option == "remove":
            item = input("Enter item to remove: ").lower()
            quantity = int(input("Enter quantity to remove: "))
            remove_from_cart(cart, item, quantity)
        elif option == "total":
            view_cart(cart, menu)
        elif option == "menu":
            display_menu(menu)
        elif option == "exit":
            print("------Thanks for your shopping------")
            break
        else:
            print("Invalid option.")

if  __name__ == "__main__":
     main()

