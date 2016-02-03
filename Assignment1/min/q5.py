def is_prime(int_to_be_judged):
    for onePrimeNumber in primeAlreadyKnown:
        if int_to_be_judged % onePrimeNumber == 0:
            return False
    return True

n = input('Enter a integer N:')
n = int(n)
primeAlreadyKnown = []
for i in range(2, n):
    if is_prime(i):
        primeAlreadyKnown.append(i)
print(primeAlreadyKnown)