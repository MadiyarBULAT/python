customer_name = input("Enter customer name: ")

item_count = 0
subtotal = 0

while True:
    product_name = input("Enter product name (or 'done' to finish): ")

    if product_name.lower() == "done":
        break

    price = float(input("Enter price: "))
    subtotal += price
    item_count += 1

print()
print(f"Customer : {customer_name.upper()}")
print(f"Items : {item_count}")
print(f"Subtotal : {subtotal} KZT")
print()

if subtotal < 3000:
    discount_label = "No discount"
    discount = 0
elif subtotal < 7000:
    discount_label = "5% discount"
    discount = subtotal * 0.05
else:
    discount_label = "15% discount"
    discount = subtotal * 0.15

total = subtotal - discount

print("------------------------------")
print(f"Discount tier : {discount_label}")
print(f"Discount : {discount} KZT")
print(f"Total : {total} KZT")
print()

print(f"Name uppercase : {customer_name.upper()}")
print(f"Name lowercase : {customer_name.lower()}")
print(f"Name length : {len(customer_name)}")

if len(customer_name) > 5:
    print("Long name")
else:
    print("Short name")