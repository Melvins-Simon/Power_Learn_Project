def calculate_discout(price,discount_percentage):
    if discount_percentage >= 20:
        return price - (price * discount_percentage/100)
    else:
        return price

# TEST
print(f"DISCOUNT APPLIED: {calculate_discout(500,20)}")
print(f"NO DICOUNT APPLIED: {calculate_discout(500,15)}")