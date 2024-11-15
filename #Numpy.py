class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - Price: ${self.price:.2f}, Quantity: {self.quantity}"


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self):
        print("\n=== Add New Product ===")
        name = input("Enter product name: ")
        
        # Input validation for price
        while True:
            try:
                price = float(input("Enter price: $"))
                if price >= 0:
                    break
                print("Price cannot be negative!")
            except ValueError:
                print("Please enter a valid number!")
        
        # Input validation for quantity
        while True:
            try:
                quantity = int(input("Enter quantity: "))
                if quantity >= 0:
                    break
                print("Quantity cannot be negative!")
            except ValueError:
                print("Please enter a valid number!")

        self.products[name] = Product(name, price, quantity)
        print(f"\n{name} has been added to inventory!")

    def update_quantity(self):
        print("\n=== Update Product Quantity ===")
        self.show_products()
        name = input("Enter product name to update: ")
        
        if name in self.products:
            while True:
                try:
                    new_quantity = int(input("Enter new quantity: "))
                    if new_quantity >= 0:
                        self.products[name].quantity = new_quantity
                        print(f"\nQuantity updated for {name}!")
                        break
                    print("Quantity cannot be negative!")
                except ValueError:
                    print("Please enter a valid number!")
        else:
            print("Product not found!")

    def update_price(self):
        print("\n=== Update Product Price ===")
        self.show_products()
        name = input("Enter product name to update: ")
        
        if name in self.products:
            while True:
                try:
                    new_price = float(input("Enter new price: $"))
                    if new_price >= 0:
                        self.products[name].price = new_price
                        print(f"\nPrice updated for {name}!")
                        break
                    print("Price cannot be negative!")
                except ValueError:
                    print("Please enter a valid number!")
        else:
            print("Product not found!")

    def remove_product(self):
        print("\n=== Remove Product ===")
        self.show_products()
        name = input("Enter product name to remove: ")
        
        if name in self.products:
            del self.products[name]
            print(f"\n{name} has been removed from inventory!")
        else:
            print("Product not found!")

    def show_products(self):
        if not self.products:
            print("\nInventory is empty!")
            return
        
        print("\n=== Current Inventory ===")
        for product in self.products.values():
            print(product)

    def show_total_value(self):
        total = sum(product.price * product.quantity for product in self.products.values())
        print(f"\nTotal Inventory Value: ${total:.2f}")


def main():
    inventory = Inventory()
    
    while True:
        print("\n=== Inventory Management System ===")
        print("1. Add new product")
        print("2. Update quantity")
        print("3. Update price")
        print("4. Remove product")
        print("5. Show all products")
        print("6. Show total inventory value")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == '1':
            inventory.add_product()
        elif choice == '2':
            inventory.update_quantity()
        elif choice == '3':
            inventory.update_price()
        elif choice == '4':
            inventory.remove_product()
        elif choice == '5':
            inventory.show_products()
        elif choice == '6':
            inventory.show_total_value()
        elif choice == '7':
            print("\nThank you for using the Inventory Management System!")
            break
        else:
            print("\nInvalid choice! Please try again.")


if __name__ == "__main__":
    main()