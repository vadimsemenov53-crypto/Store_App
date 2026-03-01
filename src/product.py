from src.types_utils import ProductDict

class Product:
    """Класс для представления товара."""

    name: str
    description: str
    __price: float
    quantity: int

    __list_products: list["Product"] = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод, который инициализирует экземпляры класса."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        self.__class__.__list_products.append(self)

    @property
    def list_products(self) -> list["Product"]:
        """Метод вывода списка объектов"""
        return self.__class__.__list_products

    @classmethod
    def new_product(cls, dict_product: ProductDict) -> "Product":
        """Метод, который принимает на вход параметры товара в словаре
         и возвращать созданный объект класса Product
         Если товар с таким именем уже существует —
        увеличивает количество и выбирает более высокую цену."""
        for product in cls.__list_products:
            if product.name == dict_product['name']:

                if dict_product['price'] > product.__price:
                    product.__price = dict_product['price']

                product.quantity += dict_product['quantity']

                return product

        return cls(**dict_product)

    @property
    def price(self) -> float:
        """Метод получения стоимости товара"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Метод изменения стоимости товара, при отрицательной цене"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            answer = str(input(f'Новая цена: {new_price} < Старой: {self.__price}. Ставим новую цену?'
                               ' y (значит yes) или n (значит no): ')).strip().lower()
            if answer == 'y':
                self.__price = new_price
            else:
                print("Цена осталась прежней: ", self.__price)
        else:
            self.__price = new_price


if __name__ == '__main__':
    product_1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product_2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product_3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product_2.price)
    print(product_2.quantity)

    print(product_3.list_products)
    product_new = Product.new_product({"name": "Iphone 15",
                                     "description": "512GB",
                                     "price": 20033300.0,
                                     "quantity": 5})

    print(product_1.list_products)
    print(product_2.price)
    print(product_2.quantity)

    product_2.price = 22000
    print(product_2.price)
    print(product_2.__dict__)
