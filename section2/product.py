class Product:
    def __init__(self, product_id, name, price, stock_quantity):
        self._product_id = product_id
        self._name = name
        self.__price = price
        self.__stock_quantity = stock_quantity

    @property
    def price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")

        self.__price = value

    @property
    def stock_quantity(self):
        return self.__stock_quantity

    def set_stock_quantity(self, value):
        if value < 0:
            raise ValueError("Stock quantity cannot be negative.")

        self.__stock_quantity = value

    def to_dict(self):
        """
        Convert the Product object into a dictionary
        that can be stored as JSON.
        """

        return {
            "product_id": self._product_id,
            "name": self._name,
            "price": self.price,
            "stock_quantity": self.stock_quantity
        }