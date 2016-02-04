givenFunction = input('Enter f(x)= ')
a = input('Enter the lower bound of integration: ')
b = input('Enter the upper bound of integration: ')
n = input('Enter the number of sub-intervals: ')
a = float(a)
b = float(b)
n = int(n)
integrationResult = 0
if n > 10000:
    print('It may takes a while...')
for i in range(1, n+1):
    x = a + (b - a) / n * (i - 1 / 2)
    integrationResult += (b - a) / n * eval(givenFunction)
print('The numerical integration is ', integrationResult)
