import json
from datetime import datetime

def load_data():
    try:
        with open("inventory_data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data

def save_data(data):
    with open("inventory_data.json", "w") as file:
        json.dump(data, file)

def display_total_cost_per_product(data):
    print("\n--- Total Cost for Each Product Restock ---")
    for item, details in data.items():
        total_cost = details["cost_per_unit"] * details["quantity_per_bulk"]
        print(f"Item: {item}, Total Cost: KSH {total_cost:.2f}")

def display_total_cost_for_week(data):
    total_cost_week = sum(details["cost_per_unit"] * details["quantity_per_bulk"] for details in data.values())
    print(f"\nTotal Cost of Restock for the Week: KSH {total_cost_week:.2f}")

def delete_all_records(data):
    confirmation = input("Are you sure you want to delete all records?`2 Kindly know once deleted, all the records can not be recovered. (yes/no): ")
    if confirmation.lower() == "yes":
        data.clear()
        print("All records deleted.")
    else:
        print("Deletion canceled.")

def restock():
    data = load_data()

    while True:
        print("\n1. Add Restock Record\n2. View Saved Records\n3. Display Total Cost per Product Restock\n4. Display Total Cost for the Week\n5. Delete All Records\n6. Exit")
        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == "1":
            # Get restock details from the shopkeeper
            item = input("Enter the name of the item: ").lower()  # Convert to lowercase
            date_restocked = datetime.now().strftime("%Y-%m-%d")
            cost_per_unit = float(input("Enter the cost per unit: "))
            quantity_per_bulk = int(input("Enter the number of items in each bulk: "))

            # Save restock details
            data[item] = {
                "date_restocked": date_restocked,
                "cost_per_unit": cost_per_unit,
                "quantity_per_bulk": quantity_per_bulk
            }

            print("Restock record added successfully!")

        elif choice == "2":
            print("\n--- Saved Restock Records ---")
            for item, details in data.items():
                print(f"Item: {item}, Date Restocked: {details['date_restocked']}, Cost Per Unit: KSH {details['cost_per_unit']:.2f}, Quantity Per Bulk: {details['quantity_per_bulk']}")

        elif choice == "3":
            display_total_cost_per_product(data)

        elif choice == "4":
            display_total_cost_for_week(data)

        elif choice == "5":
            delete_all_records(data)

        elif choice == "6":
            # Save data to JSON file before exiting
            save_data(data)
            print("Data saved. Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    restock()
