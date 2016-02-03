# Question 3 (15% of this assignment): Write a program to allow a user to input a number m, and then use a while loop
#  to find the smallest integer n such that n2 is greater than m. For example, if the user inputs m = 10, your program
#  should output n = 4.

# Answer given by tavimori

import math


while True:
    m = input('Enter a number:')
    try:
        m = float(m)
        break
    except:
        print('It seems what you\'ve input is not a number')
if m <= 0:
    print('n= 0')
else:
    n = int(math.sqrt(m))+1
    print('n=',n)