finalAccountValue = input('Enter the final account value: ')
annualInterestRate = input('Enter the annual interest rate: ')
numberOfYears = input('Enter the number of years: ')
finalAccountValue = float(finalAccountValue)
annualInterestRate = float(annualInterestRate)
numberOfYears = float(numberOfYears)
initialDepositRate = finalAccountValue / (1 + annualInterestRate / 100) ** numberOfYears
print('The initial value is:', initialDepositRate)
