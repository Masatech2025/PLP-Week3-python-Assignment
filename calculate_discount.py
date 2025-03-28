def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    :param price: Original price of the item
    :param discount_percent: Discount percentage to apply
    :return: Final price after discount or original price if no discount is applied
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

   
    final_price = calculate_discount(original_price, discount_percentage)

   
    if discount_percentage >= 20:
        print("The final price after a discount of {}% is: ${:.2f}".format(discount_percentage, final_price))
    else:
        print("No discount applied. The original price is: ${:.2f}".format(final_price))
except ValueError:
    print("Please enter a valid number.")