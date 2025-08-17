def calculate_discount(price, discount_percent):
  """
  Calculates the final price after applying a discount.

  Args:
    price: The original price of the item.
    discount_percent: The percentage of the discount.

  Returns:
    The final price after the discount is applied. 
    If the discount is less than 20%, it returns to the original price.
  """
  if discount_percent >= 20:
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price
  else:
    return price

# Now the next stage is to prompt the user for input
try:
  original_price = float(input("Enter the original price of the item: "))
  discount = float(input("Enter the discount percentage: "))

  # We then calculate the final price using the function
  final_price = calculate_discount(original_price, discount)

  # Finally we print the result
  if final_price == original_price:
    print(f"No discount applied. The final price is: ${final_price:.2f}")
  else:
    print(f"Discount applied! The final price is: ${final_price:.2f}")

except ValueError:
  print("Invalid input. Please enter valid numbers for price and discount.")