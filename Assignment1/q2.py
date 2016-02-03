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