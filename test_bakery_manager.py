from bakery_manager import calculate_order_total, update_inventory

def test_calculate_order_total():
    inventory = {"B01": {"price": 2.5, "quantity": 10}}
    order = [("B01", 2)]
    totals = calculate_order_total(order, inventory, tax_rate=0.1)
    assert round(totals["subtotal"], 2) == 5.00
    assert round(totals["tax"], 2) == 0.50
    assert round(totals["total"], 2) == 5.50

def test_update_inventory():
    inventory = {"B01": {"name": "Cupcake", "price": 2.5, "quantity": 5}}
    order = [("B01", 2)]
    updated = update_inventory(order, inventory)
    assert updated["B01"]["quantity"] == 3