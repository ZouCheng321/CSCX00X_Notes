# Question 2 (15% of this assignment): Write a program that prompts the user to enter an integer and displays the
#  number in reverse order. Here is a sample run:

# Answers given by tavimori


while True:
    integerEnterByUser = input('Enter an integer:')
    try:
        integerEnterByUser = int(integerEnterByUser)
        break
    except:
        print('It seems what you\'ve input is not an integer...')
integerEnterByUser = str(integerEnterByUser)
for i in integerEnterByUser:
    print(i)