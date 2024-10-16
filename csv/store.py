
def read_from_database(): 
    products = [] 
    try: 
        with open("product.csv", "r") as f: 
            big_text = f.read() 
            products_list = big_text.strip().split("n") 
            for line in products_list: 
                info = line.split(",") 
                products.append({'id': info[0].strip(), 'name': info[1].strip(), 'price': info[2].strip(), 'count': info[3].strip()}) 
    except Exception as e: 
        print(f"Error reading from database: {e}") 
    return products 

def add(id, name, price, count): 
    database = 'product.csv' 
    with open(database, 'a') as file: 
        file.write(f"{id},{name},{price},{count}n") 

def search(): 
    data = read_from_database() 
    user_input = input("Enter a product name to search: ") 
    for product in data: 
        if product['name'] == user_input: 
            print(product) 
            break 
    else: 
        print("Not found") 

def edit(): 
    data_base = read_from_database() 
    user_search = input("Enter a product name to edit: ") 

    for product in data_base: 
        if product['name'] == user_search: 
            product["name"] = input("New name: ") 
            product["price"] = input("New price: ") 
            product["count"] = input("New count: ") 
            break 
    else: 
        print("Not found")
        return

    # Write updated data back to the file
    with open("product.csv", "w") as f:
        for product in data_base:
            f.write(f"{product['id']},{product['name']},{product['price']},{product['count']}n")

def remove(): 
    data = read_from_database() 
    user_input = input("Enter a product name to remove: ") 

    updated_products = [product for product in data if product['name'] != user_input]

    # Write updated data back to the file
    with open("product.csv", "w") as f:
        for product in updated_products:
            f.write(f"{product['id']},{product['name']},{product['price']},{product['count']}n")

    if len(data) == len(updated_products):
        print("Not found")
    else:
        print(f"Removed {user_input}")

def show_all(): 
    data = read_from_database() 
    for product in data: 
        print(product) 

while True: 
    print("Add product = 1") 
    print("Product search = 2") 
    print("Product edit = 3") 
    print("Remove product = 4") 
    print("Show all = 5") 
    print("Exit = 6") 
    selection = input("Enter number 1 to 6: ") 

    if selection == '1': 
        id = input("Input ID: ").strip() 
        name = input("Enter name: ").strip() 
        price = input("Enter price: ").strip() 
        count = input("Enter count: ").strip() 
        add(id, name, price, count) 

    elif selection == '2': 
        search() 

    elif selection == "3": 
        edit() 

    elif selection == "4": 
        remove() 

    elif selection == "5": 
        show_all()  

    elif selection == "6": 
        break
