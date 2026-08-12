from product import Product
from order import Order, DiscountedOrder
from inventory import InventoryManager


def main():

    # InventoryManager automatically loads
    # existing products from data.json.
    inventory = InventoryManager()

    print("Current Inventory")
    print("-" * 40)

    for product in inventory.inventory.values():
        print(product.to_dict())

    print("\nOrders")
    print("-" * 40)

    # ---------------------------------
    # Create a normal order
    # ---------------------------------

    order = Order("ORD001")

    laptop = inventory.get_product("P001")
    mouse = inventory.get_product("P002")

    try:
        order.add_product(laptop, 1)
        order.add_product(mouse, 2)

        try:
            inventory.process_order(order)
            order.generate_invoice()
        
        except ValueError as error:
            print(f"Order failed: {error}")

    except ValueError as error:
        print(f"Order failed: {error}")    

    # ---------------------------------
    # Create a discounted order
    # ---------------------------------

    discounted_order = DiscountedOrder(order_id="ORD002", discount_percentage=10)

    keyboard = inventory.get_product("P003")
    try:
        discounted_order.add_product(laptop, 2)
        discounted_order.add_product(keyboard, 1)

        try:
            inventory.process_order(discounted_order)
            discounted_order.generate_invoice()

        except ValueError as error:
            print(f"Order failed: {error}")

    except ValueError as error:
        print(f"Order failed: {error}")

    # ---------------------------------
    # Reorder alerts
    # ---------------------------------

    print("\nREORDER ALERTS")
    print("-" * 40)

    alerts = inventory.generate_reorder_alerts()

    if alerts:

        for alert in alerts:
            print(alert)

    else:
        print("No products need reordering.")


if __name__ == "__main__":
    main()