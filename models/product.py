from utils.helper import format_float_to_str_currency


class Product:
    counter: int = 1

    def __init__(self: object, name: str, price: float) -> None:
        self.__product_code: int = Product.counter
        self.__name: str = name
        self.__price: float = price
        Product.counter += 1

    @property
    def product_code(self: object) -> int:
        return self.__product_code

    @property
    def name(self: object) -> str:
        return self.__name

    @property
    def price(self: object) -> float:
        return self.__price

    def __str__(self) -> str:
        return f"Product code: {self.product_code} \nName: {self.name} \nPrice: {format_float_to_str_currency(self.price)}"
