# shopping_bill_gst.py

def calculate_gst(price, gst_rate):
    return price * (gst_rate / 100)

def display_bill(items, gst_rate):
    print("===== SHOPPING BILL =====")
    total = 0
    for name, price in items:
        gst_amount = calculate_gst(price, gst_rate)
        total_price = price + gst_amount
        print(f"Item: {name}\n  Price: ₹{price:.2f}\n  GST @ {gst_rate}%: ₹{gst_amount:.2f}\n  Total: ₹{total_price:.2f}\n")
        total += total_price
    print("=========================")
    print(f"Grand Total: ₹{total:.2f}")

# List of items (Item Name, Price)
items = [
    ("Shampoo", 120),
    ("Soap", 40),
    ("Toothpaste", 85),
    ("Face Cream", 150)
]

# GST Rate (e.g., 18%)
gst_rate = 18

# Display the bill
display_bill(items, gst_rate)
