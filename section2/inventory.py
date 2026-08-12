from product import Product
from utils import load_data, save_data


class InventoryManager:

    def __init__(self):
        self.inventory = {}

        # This threshold is an assumption because
        # the assessment doesn't specify one.
        self.reorder_threshold = 5

        # Load persistent inventory from JSON.
        self.load_inventory()

    def load_inventory(self):
        """Load products from data.json."""

        data = load_data()

        for product_data in data["products"]:

            product = Product(
                product_id=product_data["product_id"],
                name=product_data["name"],
                price=product_data["price"],
                stock_quantity=product_data["stock_quantity"]
            )

            self.inventory[product._product_id] = product

    def save_inventory(self):
        """Save the current inventory to data.json."""

        data = {
            "products": [
                product.to_dict()
                for product in self.inventory.values()
            ]
        }

        save_data(data)

    def add_product(self, product):
        """Add a product to the inventory."""

        self.inventory[product._product_id] = product

        # Persist the change immediately.
        self.save_inventory()

    def get_product(self, product_id):
        return self.inventory.get(product_id)

    def process_order(self, order):
        """
        Validate the entire order first.
        Only deduct stock if everything is available.
        """

        # -----------------------------
        # STEP 1: Validate everything
        # -----------------------------

        for item in order.items:

            product = item["product"]
            quantity = item["quantity"]

            stored_product = self.get_product(
                product._product_id
            )

            if stored_product is None:
                raise ValueError(
                    f"{product.name} is not in inventory."
                )

            if quantity > stored_product.stock_quantity:
                raise ValueError(
                    f"Not enough stock for {product.name}. "
                    f"Available: {stored_product.stock_quantity}"
                )

        # -----------------------------
        # STEP 2: Deduct stock
        # -----------------------------

        for item in order.items:

            product = item["product"]
            quantity = item["quantity"]

            stored_product = self.get_product(
                product._product_id
            )

            new_quantity = stored_product.stock_quantity - quantity

            stored_product.set_stock_quantity(new_quantity)

        # -----------------------------
        # STEP 3: Persist changes
        # -----------------------------

        self.save_inventory()

        print(
            f"Order {order.order_id} "
            f"completed successfully."
        )

    def generate_reorder_alerts(self):

        alerts = []

        for product in self.inventory.values():

            if product.stock_quantity <= self.reorder_threshold:

                alerts.append(
                    f"REORDER ALERT: {product._name} "
                    f"has only {product.stock_quantity} "
                    f"units remaining."
                )

        return alerts