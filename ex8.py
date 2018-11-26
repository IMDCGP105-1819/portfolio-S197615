total_cost = input("Enter the cost of your dream home: ")
portion_deposit = float(total_cost) * 0.2
current_savings = 0
r = 1.04
annual_salary = input("Enter your annual salary: ")
portion_saved = input("Enter the percent of your salary to save, as a decimal: ")
months = 0
semi_annual_raise = input("Enter a semi annual raise as a decimal: ")
semi_annual_raise = float(semi_annual_raise) + 1
counter = 0

while current_savings < portion_deposit:
    pay_rise = float(annual_salary) * float(semi_annual_raise)
    monthly_salary = int(annual_salary) / 12
    monthly_input = float(monthly_salary) * float(portion_saved)
    current_savings = current_savings * r
    current_savings = current_savings + monthly_input
    months = months + 1
    counter = counter + 1
    if counter / 6 == 1:
        annual_salary = pay_rise
        counter = 0

else:
    print("Number of months: " + str(months))