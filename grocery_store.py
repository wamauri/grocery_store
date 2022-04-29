from datetime import datetime, time
from typing import List, Dict
from time import sleep

from utils.helper import format_float_to_str_currency
from models.product import Product

products: List[Product] = []
cart: List[Dict[Product, int]] = []


def main() -> None:
    try:
        menu()
    except KeyboardInterrupt:
        print("\nYou left the GroceryStore! Welcome back anytime!")
        sleep(1)


def menu() -> None:
    print("+----------------------------------------+")
    print("|<<<<<<<<<<<<<< Welcome to >>>>>>>>>>>>>>|")
    print("|<<<<<<<<<<<<< GroceryStore >>>>>>>>>>>>>|")
    print("+----------------------------------------+\n")

    print("Select an option below:")
    print("+-----------------------+")
    print("| 1 - Register Product  |")
    print("| 2 - List Products     |")
    print("| 3 - Bay Product       |")
    print("| 4 - View Cart         |")
    print("| 5 - Close Order       |")
    print("| 6 - Exit              |")
    print("+-----------------------+\n")

    option: int = int(input("Option: "))
    print()

    if option == 1:
        register_product()
    elif option == 2:
        list_products()
    elif option == 3:
        bay_product()
    elif option == 4:
        view_product()
    elif option == 5:
        close_order()
    elif option == 6:
        greeting()
        sleep(2)
        exit(0)
    else:
        print("Invalid Option. Try again.")
        menu()


def register_product() -> None:
    print("Register of Product")
    print("-------------------")

    name: str = input("Type the product name: ")
    price: float = float(input("Type the product price (format -> 100.00): "))

    new_product: Product = Product(name, price)

    products.append(new_product)

    print(f"The product {new_product.name} was successfully registered!")
    sleep(2)
    menu()


def list_products() -> None:
    if len(products) > 0:
        print("List products")
        print("--------------------------")
        for product in products:
            print(product)
            print("--------------------------")
            sleep(1)
    else:
        print("No products have been registered yet.")
    sleep(2)
    menu()


def bay_product() -> None:
    if len(products) > 0:
        print("Inform the product code that you want to add to cart")
        print("----------------------------------------------------")
        print("<<<<<<<<<<<<<<<< Available Products >>>>>>>>>>>>>>>>")
        for product in products:
            print(product)
            print("----------------------------------------------------")
            sleep(1)
        product_code: int = int(input("Product code: "))

        product: Product = get_product_by_code(product_code)

        if product:
            if len(cart) > 0:
                has_in_cart: bool = False
                for item in cart:
                    quantity: int = item.get(product)
                    if quantity:
                        item[product] = quantity + 1
                        print(f"The product {product.name} now has {quantity + 1} unites in cart.")
                        has_in_cart = True
                        sleep(2)
                        menu()
                if not has_in_cart:
                    p: dict = {product: 1}
                    cart.append(p)
                    print(f"The product [{product.name}] was added to cart")
                    sleep(2)
                    menu()
            else:
                item: dict = {product: 1}
                cart.append(item)
                print(f"The product {product.name} was added to cart")
                sleep(2)
                menu()
        else:
            print(f"The product with the code: {product_code} was not found")
            sleep(2)
            menu()
    else:
        print("There are no products to sell yet.")
    sleep(2)
    menu()


def view_product() -> None:
    if len(cart) > 0:
        print("Product in cart")
        print("--------------------")

        for item in cart:
            for data in item.items():
                print(data[0])
                print(f"Quantity: {data[1]}")
                print("--------------------")
                sleep(1)
    else:
        print("There are no products in the cart.")
    sleep(2)
    menu()


def close_order() -> None:
    if len(cart) > 0:
        total_value: float = 0
        print("Cart items:")
        print("--------------------------")

        for item in cart:
            for data in item.items():
                print(data[0])
                print(f"Quantity: {data[1]}")
                total_value += data[0].price * data[1]
                print("--------------------------")
                sleep(1)
        print(f"Your bill is {format_float_to_str_currency(total_value)}")
        greeting()
        cart.clear()
        sleep(5)
    else:
        print("There are no products in the cart.")
    sleep(2)
    menu()


def get_product_by_code(product_code: int) -> Product:
    p: Product = None

    if len(products) > 0:
        for product in products:
            if product.product_code == product_code:
                p = product
    else:
        print("No products have been registered yet.")
    sleep(1)

    return p


def greeting() -> None:
    now = datetime.now()
    now_time = now.time()

    if now_time <= time(00,00) or now_time >= time(18,00):
        print("Thanks for using GroceryStore! Have a good night.")
    else:
        print("Thanks for using GroceryStore! Have a good day.")


if __name__ == "__main__":
    main()
