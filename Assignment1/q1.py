# Question 1 (10% of this assignment): Suppose you want to deposit a certain amount of money into a savings account with
#  a fixed annual interest rate. What amount do you need to deposit in order to have $5,000 in the account after three
#  years? The initial deposit amount can be obtained using the following formula:
# Write a program that prompts the user to enter final account value, annual interest rate in percent, and the number
#  of years, and displays the initial deposit amount. A sample run of your program:

# Answer given by tavimori

finalAccountValue = input('Enter the final account value: ')
annualInterestRate = input('Enter the annual interest rate: ')
numberOfYears = input('Enter the number of years: ')
finalAccountValue = float(finalAccountValue)
annualInterestRate = float(annualInterestRate)
numberOfYears = float(numberOfYears)
initialDepositRate = finalAccountValue / (1 + annualInterestRate / 100) ** numberOfYears
print('The initial value is:', initialDepositRate)
