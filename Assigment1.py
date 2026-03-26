# a) Input & Variables

customer_name = input("Enter customer name: ")
product_name = input("Enter product name: ")
price = float(input("Enter price per unit (KZT): "))
quantity = int(input("Enter quantity: "))

# b) Calculations

subtotal = price * quantity

if subtotal > 5000:
    discount = subtotal * 0.10
else:
    discount = 0

total = subtotal - discount

# c) Formatted Output

print("-" * 30)
print("        SHOP RECEIPT")
print("-" * 30)

print(f"Customer : {customer_name}")
print(f"Product  : {product_name}")
print(f"Price    : {price} KZT")
print(f"Quantity : {quantity}")

print("-" * 30)

print(f"Subtotal : {subtotal} KZT")
print(f"Discount : {discount} KZT")
print(f"Total    : {total} KZT")

print("-" * 30)

# d) Comparison

discount_applied = subtotal > 5000
paid_more_than_3000 = total > 3000

print(f"Discount applied: {discount_applied}")
print(f"Paid more than 3000: {paid_more_than_3000}")