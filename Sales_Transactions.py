import json
from datetime import datetime

def load_product_details():
    try:
        with open("product_details.json", "r") as file:
            product_details = json.load(file)
    except FileNotFoundError:
        product_details = {}
    return product_details

def save_product_details(product_details):
    with open("product_details.json", "w") as file:
        json.dump(product_details, file)

def load_sales():
    try:
        with open("sales_data.json", "r") as file:
            sales_data = json.load(file)
    except FileNotFoundError:
        sales_data = []
    return sales_data

def save_sales(sales_data):
    with open("sales_data.json", "w") as file:
        json.dump(sales_data, file)

def add_sale():
    product_details = load_product_details()
    sales_data = load_sales()

    # Get sale details from the shopkeeper
    item = input("Enter the name of the product: ").lower()  # Convert to lowercase

    if item not in product_details:
        print(f"Product '{item}' not found in product details. Please add the product details first.")
        return

    selling_price = product_details[item]["selling_price"]
    quantity_sold = int(input("Enter the quantity sold:"))

    # Calculate and save total revenue
    total_revenue = selling_price * quantity_sold

    # Save sale record details
    sale_record = {
        "item": item,
        "selling_price": selling_price,
        "quantity_sold": quantity_sold,
        "total_revenue": total_revenue,
        "date_sold": datetime.now().strftime("%Y-%m-%d")
    }

    sales_data.append(sale_record)
    print("Sale record added successfully!")

    # Save data to JSON file
    save_sales(sales_data)

def view_sales():
    product_details = load_product_details()
    sales_data = load_sales()

    # Display all saved sale records
    if sales_data:
        print("\n--- Sales Records ---")
        for sale_record in sales_data:
            item = sale_record.get('item', 'N/A').lower()  # Convert to lowercase
            date_sold = sale_record.get('date_sold', 'N/A')

            # Retrieve selling price from product details
            selling_price = product_details.get(item, {}).get('selling_price', 0.0)

            quantity_sold = sale_record.get('quantity_sold', 0)
            total_revenue = sale_record.get('total_revenue', 0.0)

            print(f"Item: {item}, Date Sold: {date_sold}, Selling Price: KSH {selling_price:.2f}, Quantity Sold: {quantity_sold}, Total: KSH {total_revenue:.2f}")
    else:
        print("\nNo records available.")

def delete_all_sales():
    confirmation = input("Are you sure you want to delete all sales records? (yes/no): ")
    if confirmation.lower() == "yes":
        sales_data = []
        print("All sales records deleted.")
        save_sales(sales_data)
    else:
        print("Deletion canceled.")

if __name__ == "__main__":
    while True:
        print("\n1. Add Sale Record\n2. View Sales Records\n3. Delete All Records\n4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            add_sale()

        elif choice == "2":
            view_sales()

        elif choice == "3":
            delete_all_sales()

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
