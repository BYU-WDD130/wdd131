# -----------------------------------------------------------
# Program: Red Rose Desserts Receipt Generator
# Author: [Dery Henriquez]
# Date: [2025-10-04]
#
# Description:
# This program reads product and request data from two CSV files,
# then prints a formatted receipt with store details, totals, and tax.
#
# Enhancements (Exceeds Requirements):
# 1. Added store name and decorative header for professionalism.
# 2. Added formatted date and time using the datetime module.
# 3. Implemented a 6% sales tax calculation and displayed totals.
# 4. Improved receipt readability with aligned columns and separators.
# 5. Added exception handling for both FileNotFoundError and KeyError
#    with clear, user-friendly messages.
# 6. Included a thank-you message at the bottom of the receipt.
# 7. Clean, readable code with comments for maintainability.
# -----------------------------------------------------------

import csv
from datetime import datetime

def read_dictionary(filename):
    """Reads a CSV file and returns a dictionary where the first column is the key."""
    dictionary = {}
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # skip header
            for row in reader:
                if row:
                    key = row[0].strip()
                    dictionary[key] = [row[1].strip(), row[2].strip()]
        return dictionary
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return {}

def main():
    SALES_TAX_RATE = 0.06  # 6% sales tax

    try:
        # Step 1: Load product data
        products_dict = read_dictionary('products.csv')

        # Step 2: Print store header and date
        print("===================================")
        print("        Red Rose Desserts")
        print("===================================")
        print(f"Date: {datetime.now():%A, %B %d, %Y %I:%M %p}")
        print("-----------------------------------")
        print("Receipt:")

        # Step 3: Process customer requests
        with open('request.csv', 'r', newline='') as request_file:
            reader = csv.reader(request_file)
            next(reader)  # Skip header

            total_items = 0
            subtotal = 0.0

            for row in reader:
                if row:
                    product_number = row[0].strip()
                    quantity = int(row[1].strip())

                    try:
                        product_name, product_price = products_dict[product_number]
                        price = float(product_price)
                        line_total = price * quantity
                        total_items += quantity
                        subtotal += line_total
                        print(f"{product_name:25} x{quantity:<3} @ ${price:<6.2f} = ${line_total:>6.2f}")
                    except KeyError:
                        print(f"Error: Product ID '{product_number}' not found in product list.")

            # Step 4: Compute totals
            sales_tax = subtotal * SALES_TAX_RATE
            total = subtotal + sales_tax

            print("-----------------------------------")
            print(f"Items: {total_items}")
            print(f"Subtotal: ${subtotal:.2f}")
            print(f"Sales Tax (6%): ${sales_tax:.2f}")
            print(f"Total: ${total:.2f}")
            print("-----------------------------------")
            print("Thank you for shopping at Red Rose Desserts!")
            print("===================================")

    except FileNotFoundError:
        print("Error: 'request.csv' file not found. Please make sure it exists in your directory.")

if __name__ == "__main__":
    main()