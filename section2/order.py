class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.items = []

    def add_product(self, product, quantity):

        if quantity <= 0:
            raise ValueError(
                "Quantity must be greater than zero."
            )

        if quantity > product.stock_quantity:
            raise ValueError(
                f"Not enough stock for {product._name}."
            )

        self.items.append({
            "product": product,
            "quantity": quantity
        })

    def calculate_total(self):

        total = 0

        for item in self.items:

            product = item["product"]
            quantity = item["quantity"]

            total += product.price * quantity

        return total

    def calculate_discount(self):
        return 0

    def final_total(self):

        subtotal = self.calculate_total()
        discount = self.calculate_discount()

        return subtotal - discount

    def generate_invoice(self):

        print("=" * 60)
        print(f"ORDER #{self.order_id}")
        print("=" * 60)

        for item in self.items:

            product = item["product"]
            quantity = item["quantity"]

            line_total = product.price * quantity

            print(
                f"{product._name:<25}"
                f"{quantity:>5}"
                f"${product.price:>10.2f}"
                f"${line_total:>12.2f}"
            )

        print("-" * 60)

        subtotal = self.calculate_total()
        discount = self.calculate_discount()
        total = self.final_total()

        print(f"{'Subtotal':>48} ${subtotal:>9.2f}")
        print(f"{'Discount':>48} ${discount:>9.2f}")
        print(f"{'Grand Total':>48} ${total:>9.2f}")

        print("=" * 60)


class DiscountedOrder(Order):

    def __init__(self, order_id, discount_percentage):

        super().__init__(order_id)

        self.discount_percentage = discount_percentage

    def calculate_discount(self):

        subtotal = self.calculate_total()

        return subtotal * (
            self.discount_percentage / 100
        )