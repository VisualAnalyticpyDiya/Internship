import csv
with open('sales_data.csv', mode='r')as file:
    reader = csv.DictReader(file)
    product_total={}
    for row in reader:
        try:
            product = row['product']
            quantity = int(row['quantity'])
            price = float(row['price'])
            rev = quantity * price
            if product in product_total:
                product_total[product] += rev
            else:
                product_total[product]=rev
        except ValueError:
                print(f"Skipping a row because of missing or invalid data for: {row['product']}")
                continue
top_product=""
max_rev=0
        
for product, total in product_total.items():
             if total > max_rev:
                max_rev=total
                top_product=product
                print("totalm revenue per product:")
                for product , total in product_total.items():
                     print(f"{product}: {total:,.2f}")
                     print("-"*30)
                     print(f"top-selling product: {top_product} (${max_rev:,.2f})")
                     
