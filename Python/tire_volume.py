# This program calculates tire volume, finds prices, and logs purchase info.

import math
from datetime import datetime

# --- Constants ---
mm_per_inch = 25.4
mm3_per_liter = 1_000_000

# --- Tire Prices Data ---
# Stores example prices for various tire sizes: (width, aspect_ratio, diameter): price
tire_prices = {
    (185, 50, 14): 89.99,
    (205, 60, 15): 105.50,
    (205, 65, 15): 112.75,
    (215, 55, 16): 125.00,
    (225, 45, 17): 140.25,
    (235, 75, 15): 95.00,
    (175, 70, 13): 75.00,
    (195, 65, 15): 99.99
}

print("> pthon tire_volume.py")

# --- Get Tire Dimensions ---
# Loops to ensure positive input for width, aspect ratio, and diameter.
while True:
    width = (input("Enter the width of the tire in mm (ex. 205): "))
    width_mm = float(width)
    if width_mm <= 0:
        print("Width must be greater than zero, Try again")
        continue
    break

while True:
    aspect_ratio = (input("Enter the aspect ratio of the tire (ex. 60): "))
    aspect_ratio_percent = float(aspect_ratio)
    if aspect_ratio_percent <= 0:
        print("Aspect Ratio must be greater than zero, Try again")
        continue
    break

while True:
    diameter = (input("Enter the diameter of the wheel in inches (ex. 15) "))
    diameter_inches = float(diameter)
    if diameter_inches <= 0:
        print("Diameter must be greater than zero, Try again")
        continue
    break

# --- Find and Print Tire Price ---
user_tire_size = (width_mm, aspect_ratio_percent, diameter_inches)

if user_tire_size in tire_prices:
    found_price = tire_prices[user_tire_size]
    print(f"Price for this tire size: ${found_price:.2f}")
else:
    print("Price for this exact tire size is not listed.")

# --- Calculate Tire Volume ---
# Uses the formula: V = (π * w^2 * a * (w * a + 2540 * d)) / 10,000,000,000
# 'w' is width_mm, 'a' is aspect_ratio_percent, 'd' is diameter_inches.
volume_numerator = (math.pi * (width_mm**2) * aspect_ratio_percent *
                   ( (width_mm * aspect_ratio_percent) + (2540 * diameter_inches) ) )

volume_liters = volume_numerator / 10_000_000_000

print(f"The approximate volume is {volume_liters:.2f} liters")

# --- Purchase Inquiry ---
customer_number = "N/A" # Default if no phone number is provided
buy_choice = input("Do you want to buy tires with these dimensions? (yes/no): ").lower()

if buy_choice == 'yes':
    customer_number = input("Please enter your phone number: ")
    print("Thank you! We'll contact you shortly.")
elif buy_choice == 'no':
    print("No problem! Let us know if you change your mind.")
else:
    print("Invalid choice. Skipping Phone number collection")

# --- Log Data to File ---
current_log_time = datetime.now() # Get current date and time
formatted_date = current_log_time.strftime("%Y-%m-%d") # Format date as YYYY-MM-DD

file_name = "volumes.txt"

try:
    with open(file_name, 'a') as file_object: # Open file in append mode
        log_line = (
            f"{formatted_date}, " # Current date
            f"{width_mm}, "       # Tire width
            f"{aspect_ratio_percent}, " # Aspect ratio
            f"{diameter_inches}, " # Wheel diameter
            f"{volume_liters:.2f}, " # Tire volume
            f"(+{customer_number})\n" # Customer phone number
        )
        file_object.write(log_line) # Write the data line
except Exception as e:
    print(f"Error appending data to file: {e}")

# --- Display File Content ---
print("\nvolume.txt output")
try:
    with open(file_name, 'r') as file_object: # Open file in read mode
        print(file_object.read(), end='') # Read and print all file content
except FileNotFoundError:
    print(f"Error: The file {file_name} was not found")
except Exception as e:
    print(f"Error reading data from file: {e}")