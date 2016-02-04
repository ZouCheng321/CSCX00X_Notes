import math


m = input('Enter a number:')
m = float(m)
if m <= 0:
    print('n= 0')
else:
    n = int(math.sqrt(m))+1
    print('n=',n)