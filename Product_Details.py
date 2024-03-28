import json

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

def add_product():
    product_details = load_product_details()

    while True:
        print("\n1. Add Product\n2. View Product Details\n3. Delete All Records\n4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            # Get product details from the shopkeeper
            product_name = input("Enter the name of the product: ").lower()  # Convert to lowercase
            selling_price = float(input("Enter the selling price per unit: "))

            # Save product details
            product_details[product_name] = {
                "selling_price": selling_price
            }

            print("Product details added successfully!")

        elif choice == "2":
            print("\n--- Product Details ---")
            for product, details in product_details.items():
                print(f"Product: {product}, Selling Price: KSH {details['selling_price']:.2f}")

        elif choice == "3":
            delete_confirmation = input("Are you sure you want to delete all records? (yes/no): ")
            if delete_confirmation.lower() == "yes":
                product_details.clear()
                print("All records deleted.")
            else:
                print("Deletion canceled.")

        elif choice == "4":
            # Save data to JSON file before exiting
            save_product_details(product_details)
            print("Data saved. Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

        # Save product details to the JSON file after each operation
        save_product_details(product_details)

if __name__ == "__main__":
    add_product()
