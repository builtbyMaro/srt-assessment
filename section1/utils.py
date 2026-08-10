def calculate_discount(order_total:float, user_tier:str, promo_code:str) -> float:
    """
    user_tier choices => STANDARD (0% discount), GOLD(10% discount), VIP(20% discount)
    if order_total more than 500.00 adds a 5% discount
    if promo_code is valid adds a 3% discount
    """

    # new total to be returned
    new_total = None

    # discount based on user_tier
    match user_tier:
        case "STANDARD":
            pass
        case "GOLD":
            order_total = order_total * (1 - 10 / 100)
        case "VIP":
            order_total = order_total * (1 - 20 / 100)
        case _:
            return f"{user_tier} is not a valid user tier."

    # 5% discount if order_total greater than $500
    if order_total > 500:
        new_total = order_total * (1 - 5 / 100)

    # Additional promo logic
    promo_codes = ("WXYZ2", "RTC25", "WXWYT", "LVYST")

    if promo_code in promo_codes:
        new_total = new_total * (1 - 3 / 100)

    return new_total