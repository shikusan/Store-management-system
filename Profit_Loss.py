import json

def load_product_details():
    try:
        with open("product_details.json", "r") as file:
            product_details = json.load(file)
    except FileNotFoundError:
        product_details = {}
    return product_details

def load_cost_details():
    try:
        with open("inventory_data.json", "r") as file:
            cost_details = json.load(file)
    except FileNotFoundError:
        cost_details = {}
    return cost_details

def load_sales():
    try:
        with open("sales_data.json", "r") as file:
            sales_data = json.load(file)
    except FileNotFoundError:
        sales_data = []
    return sales_data

def calculate_remaining_stock(product_details, sales_data):
    remaining_stock = {}

    for product, details in product_details.items():
        initial_stock = details.get("initial_stock", 0)
        total_sold = sum(sale['quantity_sold'] for sale in sales_data if sale['item'] == product)
        remaining_stock[product] = initial_stock - total_sold

    return remaining_stock

def calculate_total_profit_loss(product_details, cost_details, sales_data):
    total_profit_loss = 0

    for sale in sales_data:
        item = sale['item']
        quantity_sold = sale['quantity_sold']
        selling_price = product_details[item]['selling_price']
        cost_per_unit = cost_details[item]['cost_per_unit']
        total_cost = cost_per_unit * quantity_sold
        total_revenue = selling_price * quantity_sold
        total_profit_loss += (total_revenue - total_cost)

    return total_profit_loss

def view_profit_loss_per_product(product_details, cost_details, sales_data):
    print("\n--- Profit/Loss per Product ---")
    for product in product_details:
        total_sold = sum(sale['quantity_sold'] for sale in sales_data if sale['item'] == product)
        selling_price = product_details[product]['selling_price']
        cost_per_unit= cost_details[product]['cost_per_unit']
        total_cost = cost_per_unit * total_sold
        total_revenue = selling_price * total_sold
        profit_loss = total_revenue - total_cost
        print(f"Product: {product}, Profit/Loss: KSH {profit_loss:.2f}")

def view_total_profit_loss(product_details, cost_details, sales_data):
    total_profit_loss = calculate_total_profit_loss(product_details, cost_details, sales_data)
    print(f"\nTotal Profit/Loss for the Shop: KSH {total_profit_loss:.2f}")

def view_remaining_stock(product_details, sales_data):
    remaining_stock = calculate_remaining_stock(product_details, sales_data)
    print("\n--- Remaining Stock per Product ---")
    for product, stock in remaining_stock.items():
        print(f"Product: {product}, Remaining Stock: {stock}")

if __name__ == "__main__":
    product_details = load_product_details()
    cost_details = load_cost_details()
    sales_data = load_sales()

    view_profit_loss_per_product(product_details, cost_details, sales_data)
    view_total_profit_loss(product_details, cost_details, sales_data)
    view_remaining_stock(product_details, sales_data)
