total_cost = input("Enter the cost of your dream home: ")
portion_deposit = float(total_cost) * 0.2
current_savings = 0
r = 1.04
annual_salary = input("Enter your annual salary: ")
portion_saved = input("Enter the percent of your salary to save, as a decimal: ")
monthly_salary = int(annual_salary)/12
monthly_input = float(monthly_salary) * float(portion_saved)
months = 0
semi_annual_raise = input("Enter a semi annual raise as a decimal: ")

while current_savings < portion_deposit:
    current_savings = current_savings * r
    current_savings = current_savings + monthly_input
    months = months + 1
    pay_rise = months /6
    if pay_rise == type(int) > 0:
        annual_salary = annual_salary * semi_annual_raise
else:
    print("Number of months: " + str(months))

