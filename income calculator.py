# Hours and pay input
hours = float(input('Type how many hours a week you work: '))
hourly_pay = float(input('Enter how much you earn an hour: $'))

# New hourly pay after taxes
hourly_pay = hourly_pay - hourly_pay *.20

# Math for weekly pay, biweekly pay, monthly pay, and total salary
weekly_pay = float(hourly_pay) * float(hours)
biweekly_pay = float(weekly_pay) * 2
monthly_pay = float(biweekly_pay)  * 2
total_salary = monthly_pay * 12

# Monthly expenses calculator
print('Now it is time to enter your monthly expenses')
rent = float(input('Rent: $'))
car_insurance = float(input('Car insurance: $'))
internet = float(input('Internet: $'))
gas = float(input('Gas: $'))
food = float(input('Food: $'))
subscriptions = float(input('Monthly subscriptions (including phone): $'))
other = float(input('Other (enter 0 if none): $'))
savings = float(input('Savings: $'))
utilities = rent + food + car_insurance + gas + internet + subscriptions + savings + other

# income with utilities included
annual_savings = savings * 12
gross_monthly = float(monthly_pay) - float(utilities)
expected_salary = float(gross_monthly) * 12

# 3 yrs and 5 yrs
gross_three_years = expected_salary * 3
gross_savings_three_years = annual_savings * 3
gross_five_years = expected_salary * 5
gross_savings_five_years = annual_savings * 5

# Print 
print('----------------------------------------')
print('Weekly paycheck: $' + str(weekly_pay))
print('Biweekly paycheck: $' + str(biweekly_pay))
print('Monthly paycheck: $' + str(monthly_pay))
print('Expected annual salary: $' + str(total_salary))
print('----------------------------------------')
print('Monthly utilitiy & savings cost: $-' + str(utilities))
print('Expected monthly income (after utilities & savings): $' +  str(gross_monthly))
print('Expected annual income (after utilities & savings) : $' + str(expected_salary))
print('Expected yearly savings: $' + str(annual_savings))
print('----------------------------------------')
print('Expected income after 3 years: $' +  str(gross_three_years))
print('Expected savings after 3 years: $' + str(gross_savings_three_years))
print('Expected income after 5 years: $' + str(gross_five_years))
print('Expected savings after 5 years: $' + str(gross_savings_five_years))