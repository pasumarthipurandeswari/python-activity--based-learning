
# Manufacturing Cost and Profitability Analysis

# Input details
material_cost = float(input("Enter material cost: "))
labour_charges = float(input("Enter labour charges: "))
wastage_percentage = float(input("Enter wastage percentage: "))
machine_cost = float(input("Enter machine cost: "))
selling_price = float(input("Enter selling price per product: "))
quantity = int(input("Enter number of products: "))
profit_target = float(input("Enter required profit percentage: "))

# Calculate wastage cost
wastage_cost = material_cost * wastage_percentage / 100

# Calculate total production cost
total_cost = (material_cost + labour_charges +
              wastage_cost + machine_cost) * quantity

# Calculate total revenue
total_revenue = selling_price * quantity

# Calculate profit or loss
profit = total_revenue - total_cost

# Calculate profit percentage
if total_cost > 0:
    profit_percentage = (profit / total_cost) * 100
else:
    profit_percentage = 0

# Display results
print("\n--- Manufacturing Cost Analysis ---")
print("Wastage Cost:", wastage_cost * quantity)
print("Total Production Cost:", total_cost)
print("Total Revenue:", total_revenue)
print("Profit/Loss:", profit)
print("Profit Percentage:", round(profit_percentage, 2), "%")

# Check profit target
if profit < 0:
    print("Result: Production is running at a loss.")
elif profit_percentage >= profit_target:
    print("Result: Profit target achieved.")
else:
    print("Result: Profit target not achieved.")
