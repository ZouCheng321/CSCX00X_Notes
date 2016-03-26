locker = [False] * 100
for i in range(100):
    for j in range(i, 100, i+1):
        locker[j] = not locker[j]
print('The opened lockers are number ', ', '.join([str(i+1) for i in range(100) if locker[i] == True]),sep='')
