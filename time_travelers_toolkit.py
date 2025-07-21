from datetime import datetime as dt
from random import randint, choice
import custom_module
from decimal import Decimal

now = dt.now()
current_date = now.date()
current_time = now.time()
base_cost = Decimal("99.99")
current_year = current_date.year
target_year = randint(1800, 3000)
base_cost = Decimal("99.99")
year_difference = abs(target_year - current_year)
cost_multiplier = Decimal(year_difference) * Decimal("10")
final_cost = (base_cost + cost_multiplier)
print(f"Current Date: {current_date}")
print(f"Current Time: {current_time}")
print(target_year)

destinations = [
    "Ancient Egypt",
    "Renaissance Florence",
    "The Moon Colony",
    "Neo Tokyo 3000",
    "Atlantis",
    "Medieval England",
    "Mars Base Alpha"
]

# Randomly select one destination
selected_destination = choice(destinations)
print(selected_destination)
message = custom_module.generate_time_travel_message(target_year, selected_destination, final_cost)

# Print the message
print(message)
