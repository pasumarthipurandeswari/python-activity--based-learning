
# Smart Canteen Order and Stock Management

# Initial inventory and prices
stock = {
    "idli": 50,
    "dosa": 30,
    "sandwich": 20,
    "juice": 25
}

prices = {
    "idli": 20,
    "dosa": 40,
    "sandwich": 50,
    "juice": 30
}

total_sales = 0
successful_orders = 0
rejected_orders = 0

print("===== SMART CANTEEN MENU =====")
for item in stock:
    print(item.title(), "- Rs.", prices[item],
          "| Available:", stock[item])

customers = int(input("\nEnter number of customer orders: "))

for i in range(customers):
    print("\nCustomer", i + 1)

    item = input("Enter food item: ").lower().strip()
    quantity = int(input("Enter quantity: "))

    # Validate order
    if item not in stock:
        print("Order rejected: Item not available in menu.")
        rejected_orders += 1

    elif quantity <= 0:
        print("Order rejected: Invalid quantity.")
        rejected_orders += 1

    elif quantity > stock[item]:
        print("Order rejected: Insufficient stock.")
        print("Available quantity:", stock[item])
        rejected_orders += 1

    else:
        # Calculate bill and update stock
        bill = prices[item] * quantity
        stock[item] -= quantity
        total_sales += bill
        successful_orders += 1

        print("Order successful!")
        print("Item:", item.title())
        print("Quantity:", quantity)
        print("Total bill: Rs.", bill)
        print("Remaining stock:", stock[item])

# Daily sales summary
print("\n===== DAILY CANTEEN REPORT =====")
print("Successful orders:", successful_orders)
print("Rejected orders:", rejected_orders)
print("Total daily sales: Rs.", total_sales)

print("\nRemaining Stock:")
for item in stock:
    print(item.title(), ":", stock[item])

print("\nDaily report completed.")
