#Discount Code-along Activity
#requirements:
#ask the user for the subtotal & day of the week
#computes and prints the discount amount
#computes and prints the sales tax amount
#total amount due
print(">python discount.py")
from datetime import datetime
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()
day_of_week = 1
#discount parameters
#if the subtotal is 50 or greater and today is Tues. or Wed. = -.10
#subtotal + (sales tax) .06% = total amount
tuesday_wednesday_discount= .10
discount_treshold = 50.00
SALES_TAX_RATE = 0.06 # Added sales tax constant

subtotal = 0.0

print("\nEnter item prices and quantities (Enter 0 for quantity to finish)")

while True:
    price_input = input("Enter price:")
    if price_input.lower() == 'exit': # Corrected: 'exit' is now a string
        print("Exiting entry")
        break
    price = float(price_input)
    if price <0:
        print("Price cannot be negative. Try again.")
        continue

    quantity_input = input("Enter Quantity: ")
    quantity = int(quantity_input)

    if quantity <0:
        print("Quantity cannot be negative. Try again")
        continue
    elif quantity == 0:
        print("Finished entering items. ")
        break

    subtotal += price * quantity
    print(f"Subtotal: {subtotal:.2f}")

if subtotal <=0:
    print("Error: The number of subtotal must be greater than zero.")
else: # All following logic is now correctly inside this else block
    discount_amount = 0.0
    discounted_subtotal = subtotal

    if subtotal >= discount_treshold and (day_of_week == 1 or day_of_week == 2):
        discount_amount = subtotal * tuesday_wednesday_discount
        discounted_subtotal = subtotal - discount_amount
        print(f"Discount amount: {discount_amount:.2f}")

    elif (day_of_week ==1 or day_of_week==2) and subtotal <discount_treshold:
        amount_needed = discount_treshold - subtotal
        print(f"No discount applied yet. Purchase ${amount_needed:.2f} more to receive the discount")

    else:
        print("No discount applied")

    # These lines are now correctly indented!
    tax_amount = discounted_subtotal * SALES_TAX_RATE # Using the constant
    total_amount_due = discounted_subtotal + tax_amount
    print(f"Sales tax amount: {tax_amount:.2f}")
    print(f"Total: {total_amount_due:.2f}")