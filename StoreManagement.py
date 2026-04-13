import pickle
import os

# ================= CLASSES =================
class Customer:
    def __init__(self, cid, name, address, mobile, dob):
        self.cid = cid
        self.name = name
        self.address = address
        self.mobile = mobile
        self.dob = dob

class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price

class Order:
    def __init__(self, cid, pid, qty):
        self.cid = cid
        self.pid = pid
        self.qty = qty

# ================= COMMON FUNCTIONS =================
def pause():
    input("\nPress Enter to continue...")

def load_data(filename):
    data = []
    if os.path.exists(filename):
        with open(filename, 'rb') as file:
            try:
                while True:
                    data.append(pickle.load(file))
            except EOFError:
                pass
    return data

def save_data(filename, data):
    with open(filename, 'wb') as file:
        for item in data:
            pickle.dump(item, file)

# ================= CUSTOMER =================
def add_customer():
    customers = load_data('customer1.bin')

    cid = input("Enter Customer ID: ")
    name = input("Enter Name: ")
    address = input("Enter Address: ")
    mobile = input("Enter Mobile: ")
    dob = input("Enter DOB: ")

    customers.append(Customer(cid, name, address, mobile, dob))
    save_data('customer1.bin', customers)

    print("Customer added successfully")
    pause()

def view_customers():
    customers = load_data('customer1.bin')

    print("\n{:<10}{:<15}{:<20}{:<15}{:<12}".format("CID", "Name", "Address", "Mobile", "DOB"))

    for c in customers:
        print("{:<10}{:<15}{:<20}{:<15}{:<12}".format(
            c.cid, c.name, c.address, c.mobile, c.dob
        ))
    pause()

def delete_customer():
    customers = load_data('customer1.bin')
    cid = input("Enter Customer ID to delete: ")

    new_list = [c for c in customers if c.cid != cid]

    if len(customers) == len(new_list):
        print("Customer not found")
    else:
        save_data('customer1.bin', new_list)
        print("Customer deleted successfully")
    pause()

# ================= PRODUCT =================
def add_product():
    products = load_data('product1.bin')

    pid = input("Enter Product ID: ")
    name = input("Enter Product Name: ")

    try:
        price = int(input("Enter Price: "))
    except:
        print("Invalid price")
        pause()
        return

    products.append(Product(pid, name, price))
    save_data('product1.bin', products)

    print("Product added successfully")
    pause()

def view_products():
    products = load_data('product1.bin')

    print("\n{:<10}{:<20}{:<10}".format("PID", "Name", "Price"))

    for p in products:
        print("{:<10}{:<20}{:<10}".format(p.pid, p.name, p.price))
    pause()

def update_product():
    products = load_data('product1.bin')
    pid = input("Enter Product ID: ")

    for p in products:
        if p.pid == pid:
            print("Old Price:", p.price)
            try:
                p.price = int(input("Enter New Price: "))
            except:
                print("Invalid price")
                pause()
                return

            save_data('product1.bin', products)
            print("Product updated successfully")
            pause()
            return

    print("Product not found")
    pause()

# ================= ORDER =================
def place_order():
    customers = load_data('customer1.bin')
    products = load_data('product1.bin')
    orders = load_data('order1.bin')

    cid = input("Enter Customer ID: ")
    customer = next((c for c in customers if c.cid == cid), None)

    if not customer:
        print("Customer not found")
        pause()
        return

    pid = input("Enter Product ID: ")
    product = next((p for p in products if p.pid == pid), None)

    if not product:
        print("Product not found")
        pause()
        return

    try:
        qty = int(input("Enter Quantity: "))
    except:
        print("Invalid quantity")
        pause()
        return

    total = product.price * qty
    print("Total Bill:", total)

    orders.append(Order(cid, pid, qty))
    save_data('order1.bin', orders)

    print("Order placed successfully")
    pause()

def view_orders():
    customers = load_data('customer1.bin')
    products = load_data('product1.bin')
    orders = load_data('order1.bin')

    print("\nAll Orders")

    for o in orders:
        customer = next((c for c in customers if c.cid == o.cid), None)
        product = next((p for p in products if p.pid == o.pid), None)

        if customer and product:
            print("\nCustomer:", customer.name)
            print("Product:", product.name)
            print("Quantity:", o.qty)
            print("Total:", product.price * o.qty)
    pause()

def view_orders_by_cid():
    cid = input("Enter Customer ID: ")

    products = load_data('product1.bin')
    orders = load_data('order1.bin')

    found = False

    for o in orders:
        if o.cid == cid:
            product = next((p for p in products if p.pid == o.pid), None)
            if product:
                found = True
                print("\nProduct:", product.name)
                print("Quantity:", o.qty)
                print("Total:", product.price * o.qty)

    if not found:
        print("No orders found for this customer")
    pause()

# ================= MENU =================
while True:
    print("""
1. Add Customer
2. View Customers
3. Delete Customer
4. Add Product
5. View Products
6. Update Product
7. Place Order
8. View Orders
9. View Orders by CID
0. Exit
""")

    choice = input("Enter choice: ")

    if choice == '1':
        add_customer()
    elif choice == '2':
        view_customers()
    elif choice == '3':
        delete_customer()
    elif choice == '4':
        add_product()
    elif choice == '5':
        view_products()
    elif choice == '6':
        update_product()
    elif choice == '7':
        place_order()
    elif choice == '8':
        view_orders()
    elif choice == '9':
        view_orders_by_cid()
    elif choice == '0':
        print("Exit")
        break
    else:
        print("Invalid Choice")
        pause()
