import csv
import datetime
import os
import tkinter as tk
from tkinter import ttk, messagebox, Frame, Label, Button
from number_entry import IntEntry

# -------------------------
# 1. Leer inventario
# -------------------------
def read_inventory(filename):
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
        messagebox.showerror("Error", f"Archivo no encontrado: {filename}")
    return inventory




# 2. Guardar inventario
# -------------------------
def save_inventory(filename, inventory):
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

# -------------------------
# 3. Calcular totales
# -------------------------
def calculate_order_total(order_list, inventory, tax_rate=0.07):
    subtotal = 0
    for item_id, qty in order_list:
        if item_id in inventory:
            subtotal += inventory[item_id]["price"] * qty
    tax = subtotal * tax_rate
    total = subtotal + tax
    return {"subtotal": subtotal, "tax": tax, "total": total}

# -------------------------
# 4. Actualizar inventario
# -------------------------
def update_inventory(order_list, inventory):
    for item_id, qty in order_list:
        if item_id in inventory:
            inventory[item_id]["quantity"] -= qty
            if inventory[item_id]["quantity"] < 0:
                inventory[item_id]["quantity"] = 0
    return inventory

# -------------------------
# 5. Generar recibo
# -------------------------
def display_receipt(order_list, totals, inventory):
    receipt = []
    receipt.append("====== Red Rose Bakery Receipt ======")
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

# -------------------------
# 6. Guardar orden
# -------------------------
def record_order(order_list, totals, filename="sales_log.csv"):
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

# -------------------------
# 7. Interfaz gráfica
# -------------------------
class BakeryApp:
    def __init__(self, master):
        self.master = master
        master.title("Red Rose Bakery")
        master.geometry("600x500")
        master.resizable(False, False)

        self.inventory_file = "inventory.csv"
        self.inventory = read_inventory(self.inventory_file)
        self.order_list = []

        # Crear tabla de productos
        self.tree = ttk.Treeview(master, columns=("ID","Name","Price","Stock","Qty"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Stock", text="Stock")
        self.tree.heading("Qty", text="Quantity")
        self.tree.pack(fill=tk.BOTH, expand=True, pady=10)

        # Llenar tabla
        for item_id, item in self.inventory.items():
            self.tree.insert("", tk.END, values=(item_id, item["name"], f"${item['price']:.2f}", item["quantity"], 0))

        # Botón de generar orden
        self.order_button = tk.Button(master, text="Process Order", command=self.process_order)
        self.order_button.pack(pady=10)

        # Área de texto para recibo
        self.receipt_text = tk.Text(master, height=15)
        self.receipt_text.pack(fill=tk.BOTH, expand=True, pady=10)

    def process_order(self):
        self.order_list.clear()
        for row in self.tree.get_children():
            values = self.tree.item(row)["values"]
            item_id, qty = values[0], values[4]
            try:
                qty = int(qty)
            except ValueError:
                qty = 0
            if qty > 0:
                if qty > self.inventory[item_id]["quantity"]:
                    messagebox.showwarning("Stock Error", f"Not enough stock for {self.inventory[item_id]['name']}")
                    return
                self.order_list.append((item_id, qty))

        if not self.order_list:
            messagebox.showinfo("Info", "No items selected.")
            return

        totals = calculate_order_total(self.order_list, self.inventory)
        receipt = display_receipt(self.order_list, totals, self.inventory)
        self.receipt_text.delete(1.0, tk.END)
        self.receipt_text.insert(tk.END, receipt)

        update_inventory(self.order_list, self.inventory)
        save_inventory(self.inventory_file, self.inventory)
        record_order(self.order_list, totals)
        messagebox.showinfo("Success", "Order recorded and inventory updated successfully!")

        # Actualizar tabla
        for row in self.tree.get_children():
            item_id = self.tree.item(row)["values"][0]
            self.tree.set(row, "Stock", self.inventory[item_id]["quantity"])
            self.tree.set(row, "Qty", 0)


# -------------------------
# 8. Ejecutar programa
# -------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = BakeryApp(root)
    root.mainloop()