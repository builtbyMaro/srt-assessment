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


print(format_sku(" shirt_blue_xl "))