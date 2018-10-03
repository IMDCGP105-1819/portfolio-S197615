cars = 100
space = 4
drivers = 30
passengers = 90
not_driven = cars - drivers
driven = drivers
carpool_capacity = driven * space
average_passengers_per_car = passengers / driven

print("There are", cars, "cars available")
print("There are only", drivers, "drivers available")
print("There will be", not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today")
print("We have", passengers, "to carpool today")
print("We need to put about", average_passengers_per_car, "in each car.")
