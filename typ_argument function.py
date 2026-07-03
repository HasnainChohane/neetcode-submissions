def calculate_bill(price=100, quantity=4, discount=10):
    total = price * quantity
    final_bill = total - (total * (discount / 100))
    return final_bill
print(calculate_bill())
