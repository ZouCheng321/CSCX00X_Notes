# Question 5 (20% of this assignment): Write a program to allow a user to input an integer N, and print all the prime
#  numbers which are smaller than N. For example, when the user inputs N = 10, your program should output
# Your program should output at most 8 prime numbers in each line. Your program should also be robust enough to handle
#  the possible improper inputs (e.g. the user inputs a string).

# Answer given by tavimori


def is_prime(int_to_be_judged):
    for onePrimeNumber in primeAlreadyKnown:
        if int_to_be_judged % onePrimeNumber == 0:
            return False
    return True

def print_a_list(list_to_be_printed):
    1+1



# Input Filtering
while True:
    n = input('Enter a integer N:')
    try:
        if float(n) == int(n) and int(n) >= 2:
            n = int(n)
            break
        else:
            print('It seems what you\'ve input is not an integer or smaller than 2')
    except:
        print('It seems what you\'ve input is not a number')
# Initializing the list of known prime numbers
primeAlreadyKnown = []
# Mapping all the possible numbers to find all primes
for i in range(2, n):
    if is_prime(i):
        primeAlreadyKnown.append(i)
print(primeAlreadyKnown)