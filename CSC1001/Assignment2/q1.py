n = float(input('n'))
nextGuess = 2
lastGuess = 1
while nextGuess != lastGuess:
    lastGuess, nextGuess = nextGuess, (lastGuess + (n / lastGuess)) / 2
print(nextGuess)