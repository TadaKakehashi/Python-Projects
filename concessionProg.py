menu = {
    "pizza": 12.99,
    "chicken-wings": 18,
    "burger": 10,
    "taco": 3.99
}

print("--------MENU--------")
for key, value in menu.items():
    print(f"{key:20}: ${value:.2f}")

total_price = 0
ordered_items = []  

while True:
    order = input("Please enter your order (q to Quit): ").lower().strip()
    if order == "q":
        break
    elif order in menu:
        total_price += menu[order]
        ordered_items.append(order)  
        print(f"{order.capitalize()} added to your order. Total so far: ${total_price:.2f}")
    else:
        print(f"Sorry, but we don't serve {order}")


print("\n--------ORDER SUMMARY--------")
if ordered_items:
    print("You ordered:")
    for item in ordered_items:
        print(f"- {item.capitalize()}")
    print(f"Total price: ${total_price:.2f}")
else:
    print("You didn't order anything. Thank you for visiting!")