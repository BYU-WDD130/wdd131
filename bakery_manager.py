import csv
import datetime
import os



# 1. Read inventory from CSV file

def read_inventory(filename):
    """Reads bakery inventory data from a CSV file and returns it as a dictionary."""
    inventory = {}
    try:
        with open(filename, "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                item_id = row["item_id"]
                inventory[item_id] = {
                    "name": row["name"],
                    "price": float(row["price"]),
                    "quantity": int(row["quantity"])
                }
    except FileNotFoundError:
        print(f"⚠️ File not found: {filename}")
    return inventory


# 2. Save updated inventory to CSV

def save_inventory(filename, inventory):
    """Writes updated inventory data back to a CSV file."""
    with open(filename, "w", newline="") as csvfile:
        fieldnames = ["item_id", "name", "price", "quantity"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item_id, item in inventory.items():
            writer.writerow({
                "item_id": item_id,
                "name": item["name"],
                "price": item["price"],
                "quantity": item["quantity"]
            })



# 3. Calculate totals

def calculate_order_total(order_list, inventory, tax_rate=0.07):
    """Computes the subtotal, sales tax, and total for a customer order."""
    subtotal = 0
    for item_id, qty in order_list:
        if item_id in inventory:
            subtotal += inventory[item_id]["price"] * qty
    tax = subtotal * tax_rate
    total = subtotal + tax
    return {"subtotal": subtotal, "tax": tax, "total": total}



# 4. Update inventory

def update_inventory(order_list, inventory):
    """Deducts product quantities from the inventory after a sale."""
    for item_id, qty in order_list:
        if item_id in inventory:
            inventory[item_id]["quantity"] -= qty
            if inventory[item_id]["quantity"] < 0:
                inventory[item_id]["quantity"] = 0
    return inventory



# 5. Display receipt

def display_receipt(order_list, totals, inventory):
    """Returns a formatted receipt for the order."""
    receipt = []
    receipt.append("\n====== Red Rose Bakery Receipt ======")
    receipt.append(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    for item_id, qty in order_list:
        if item_id in inventory:
            name = inventory[item_id]["name"]
            price = inventory[item_id]["price"]
            line_total = price * qty
            receipt.append(f"{name:<20} x{qty:<3} @ ${price:.2f} = ${line_total:.2f}")

    receipt.append("--------------------------------------")
    receipt.append(f"Subtotal: ${totals['subtotal']:.2f}")
    receipt.append(f"Tax:       ${totals['tax']:.2f}")
    receipt.append(f"Total:     ${totals['total']:.2f}")
    receipt.append("======================================")

    return "\n".join(receipt)



# 6. Record order with timestamp

def record_order(order_list, totals, filename="sales_log.csv"):
    """Saves each completed order with a timestamp to a sales log CSV file."""
    file_exists = os.path.exists(filename)
    with open(filename, "a", newline="") as csvfile:
        fieldnames = ["datetime", "item_id", "quantity", "subtotal", "tax", "total"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for item_id, qty in order_list:
            writer.writerow({
                "datetime": timestamp,
                "item_id": item_id,
                "quantity": qty,
                "subtotal": f"{totals['subtotal']:.2f}",
                "tax": f"{totals['tax']:.2f}",
                "total": f"{totals['total']:.2f}"
            })



# 7. Get user order

def get_user_order(inventory):
    """Displays available items and records the user’s selections."""
    print("\n=== Welcome to Red Rose Bakery ===")
    print("Available Items:")
    for item_id, item in inventory.items():
        print(f"{item_id}: {item['name']} - ${item['price']:.2f} (Stock: {item['quantity']})")

    order_list = []
    while True:
        item_id = input("\nEnter item ID to add (or 'done' to finish): ").strip()
        if item_id.lower() == "done":
            break
        if item_id not in inventory:
            print("❌ Invalid ID. Try again.")
            continue
        qty = int(input("Enter quantity: "))
        if qty > inventory[item_id]["quantity"]:
            print("⚠️ Not enough stock available.")
            continue
        order_list.append((item_id, qty))
    return order_list


# 8. Main program flow

def main():
    """Coordinates the main program flow — loading data, taking orders, updating inventory, and saving results."""
    inventory_file = "inventory.csv"
    inventory = read_inventory(inventory_file)

    if not inventory:
        print("⚠️ No inventory data found.")
        return

    order_list = get_user_order(inventory)
    if not order_list:
        print("No items ordered.")
        return

    totals = calculate_order_total(order_list, inventory)
    print(display_receipt(order_list, totals, inventory))

    update_inventory(order_list, inventory)
    save_inventory(inventory_file, inventory)
    record_order(order_list, totals)

    print("\n✅ Order recorded and inventory updated successfully!")



# Run the program

if __name__ == "__main__":
    main()