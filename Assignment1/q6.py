# Question 6 (25% of this assignment): Given a function f(x), and a real interval [a, b], the numerical integration of
#  f(x) over interval [a, b] can be calculated as:

# In equation (1), n represents the number of sub-intervals into which the interval [a, b] will be divided; and it
#  controls the accuracy of numerical integration.

# Write a program to allow the user to specify a trigonometric function f (f can only be sin, cos or tan), and input
#  the interval end points a, b and number of sub-intervals n. Your program should then calculate the numerical
#  integration of f over [a, b] using equation (1), and output the result. Your program should be robust enough to
#  handle possible improper inputs (e.g. the user inputs a floating point number as n).
# Python has built-in trigonometric functions. To call them, use the following statement in your program to import
#  them from the math package:
# You can then invoke the trigonometric functions like the following examples:

# Written by tavimori

givenFunction = input('Enter f(x)= ')
a = input('Enter the lower bound of integration: ')
b = input('Enter the upper bound of integration: ')
n = input('Enter the number of sub-intervals: ')
# givenFunction = '2 * x'
# lowerBoundOfIntegration = 0
# upperBoundOfIntegration = 1
# nOfSubInterval = 2
a = float(a)
b = float(b)
n = int(n)

# Initializing the result
integrationResult = 0
if n > 10000:
    print('It may takes a while...')
for i in range(1, n+1):
    # print(i)
    x = a + (b - a) / n * (i - 1 / 2)
    integrationResult += (b - a) / n * eval(givenFunction)
print('The numerical integration is ', integrationResult)
