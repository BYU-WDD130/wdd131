import csv

def read_dictionary(filename):
    """
    Reads a CSV file and returns a dictionary.
    The first column of the CSV file is used as the key.
    Each row is stored as a list (excluding the key column).
    """
    dictionary = {}
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                # Skip empty rows
                if row:
                    key = row[0]  # product number as key
                    dictionary[key] = row[1:]  # rest of the row as value
        return dictionary
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return {}

def main():
    # Step 1: Read products.csv into a dictionary
    products_dict = read_dictionary('products.csv')

    # Display the dictionary
    print("Products Dictionary:")
    for key, value in products_dict.items():
        print(key, value)

    # Step 2: Open request.csv and process requests
    try:
        with open('request.csv', 'r', newline='') as request_file:
            reader = csv.reader(request_file)
            next(reader)  # Skip the header line

            print("\nReceipt:")
            for row in reader:
                if row:  # Skip empty rows
                    product_number = row[0]
                    quantity = row[1]

                    # Look up the product in the dictionary
                    if product_number in products_dict:
                        product_name, product_price = products_dict[product_number]
                        print(f"{product_name} - Quantity: {quantity} - Price: ${product_price}")
                    else:
                        print(f"Product number {product_number} not found in products.csv")
    except FileNotFoundError:
        print("Error: request.csv file not found.")

# Protect the main call
if __name__ == "__main__":
    main()