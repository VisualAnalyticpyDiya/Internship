import csv

with open('sales_data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    
    product_totals = {}

    for row in reader:
        try:

            product = row['product']
            quantity = int(row['quantity'])
            price = float(row['price'])
        

            revenue = quantity * price
        
            if product in product_totals:
             product_totals[product] += revenue
            else:
             product_totals[product] = revenue
        except ValueError:
            print(f"Skipping a row because of missing or invalid data for: {row['product']}")
            continue
top_product = ""
max_rev = 0

for product, total in product_totals.items():
    if total > max_rev:
        max_rev = total
        top_product = product


print("Total Revenue Per Product:")
for product, total in product_totals.items():
    print(f"{product}: {total:,.2f}")


print("-" * 30)
print(f"Top-Selling Product: {top_product} (${max_rev:,.2f})")