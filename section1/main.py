from utils import calculate_discount

# Question 1
calculating_discount = False
while calculating_discount:
    try:
        # input order total
        total = float(input("Enter order total: "))

        # select user tier
        print("Select User Tier")
        print("1: STANDARD")
        print("2: GOLD")
        print("3: VIP")
        tier_choice = int(input("Enter user tier (1/2/3): "))
        if tier_choice == 1:
            user_tier = "STANDARD"
        elif tier_choice == 2:
            user_tier = "GOLD"
        elif tier_choice == 3:
            user_tier = "VIP"

        # input promo code if any
        while True:
            enter_promo_code = input("Do you have a promo code ? (Y/N): ").capitalize()
            if enter_promo_code == "Y":
                promo_code = input("Enter your promo code (case sensitive): ")
                break
            elif enter_promo_code == "N":
                promo_code = ""
                break
            else:
                print("Please enter Y/N")

        discounted_price = calculate_discount(order_total=total, user_tier=user_tier, promo_code=promo_code)
        print(f"Total: ${discounted_price:.2f}")
        break
        
    except ValueError:
        print(f"Please enter a valid input.")

# Question2
def create_reorder_manifest(inventory):
    # This dictionary will store products grouped by vendor.
    manifest = {}

    # Loop through every product in the inventory.
    for product_id, product in inventory.items():

        quantity = product["quantity"]
        threshold = product["reorder_threshold"]
        vendor = product["vendor"]

        # Reorder the product if its quantity is at or below
        # the configured reorder threshold.
        if quantity <= threshold:

            # Create the vendor entry if it doesn't exist yet.
            if vendor not in manifest:
                manifest[vendor] = []

            # Add the product information to that vendor's list.
            manifest[vendor].append({
                "product_id": product_id,
                "current_quantity": quantity,
                "reorder_threshold": threshold
            })

    return manifest


inventory = {
    "SKU001": {
        "quantity": 5,
        "reorder_threshold": 10,
        "vendor": "Vendor A"
    },
    "SKU002": {
        "quantity": 20,
        "reorder_threshold": 10,
        "vendor": "Vendor B"
    },
    "SKU003": {
        "quantity": 3,
        "reorder_threshold": 5,
        "vendor": "Vendor A"
    }
}

# print(create_reorder_manifest(inventory))

# Question 3
def format_sku(raw_sku):
    # Remove whitespace from the beginning and end.
    sku = raw_sku.strip()

    # Convert the entire SKU to uppercase.
    sku = sku.upper()

    # Split the SKU into its individual components.
    parts = sku.split("_")

    # Remove empty components in case the input contains double underscores.
    parts = [part for part in parts if part]

    # Join the components using hyphens.
    return "-".join(parts)


# print(format_sku(" shirt_blue_xl "))


# Question 6
def validate_password(password):
    errors = []

    # Check the minimum password length.
    if len(password) < 8:
        errors.append("Password must contain at least 8 characters.")

    # Check whether the password contains a number.
    has_digit = False

    for character in password:
        if character.isdigit():
            has_digit = True
            break

    if not has_digit:
        errors.append("Password must contain at least one numeric digit.")

    # Check whether the password contains one of the
    # allowed special characters.
    special_characters = "@#$"
    has_special = False

    for character in password:
        if character in special_characters:
            has_special = True
            break

    if not has_special:
        errors.append(
            "Password must contain at least one special character (@, #, $)."
        )

    # If there are no errors, the password is valid.
    if not errors:
        return {
            "valid": True,
            "message": "Password is valid."
        }

    return {
        "valid": False,
        "errors": errors
    }


# print(validate_password("hello123"))
# print(validate_password("hello123$"))

# Question 7
def remove_duplicate_order_id(order_ids):
    # A set gives us fast membership checking.
    seen = set()

    # This list will preserve the original arrival order.
    clean_orders = []

    for order_id in order_ids:

        # Only add the order if we haven't encountered it before.
        if order_id not in seen:
            seen.add(order_id)
            clean_orders.append(order_id)

    return clean_orders


orders = [102, 105, 102, 108, 110, 105]

# print(remove_duplicate_order_id(orders))