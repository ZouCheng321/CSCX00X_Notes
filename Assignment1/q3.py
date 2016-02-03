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