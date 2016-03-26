import pickle

from tkinter import *


def press_show_meaning():
    print('PressShownMeaning')


def press_next_word():
    global index
    print('PressNextWord')
    sampleLabel0.text = vocabulary[index][0]
    index += 1


# def load_words():


with open('./vocabDatabaseFile.pkl', 'rb') as pickle_file:
    vocabulary = pickle.load(pickle_file)

index = 0
root = Tk()
root.geometry('500x600+150+200')
root.title('My first GUI')

wordLabel0 = Label(root, text='Word:', height=2)
wordLabel0.grid(row=0, column=0)
wordLabel1 = Label(root, width=30, text='abash', height=2)
wordLabel1.grid(row=0, column=1)

meaningLabel0 = Label(root, text='Meaning:', height=3)
meaningLabel0.grid(row=1, column=0)
meaningLabel1 = Label(root, text='To lose self-confidence, to confuse, put to shame', height=3)
meaningLabel1.grid(row=1, column=1)

sampleLabel0 = Label(root, text='Sample:', height=3)
sampleLabel0.grid(row=2, column=0)
sampleLabel1 = Label(root, text='abashed before the assembled dignitaries', height=3)
sampleLabel1.grid(row=2, column=1)

synLabel0 = Label(root, text='Synonyms:', height=8)
synLabel0.grid(row=3, column=0)
synLabel1 = Label(root, text='fluster\ndisconcert\ndiscomfit\ndiscompose', height=8)
synLabel1.grid(row=3, column=1)

antLabel0 = Label(root, text='Antonyms:', height=8)
antLabel0.grid(row=4, column=0)
antLabel1 = Label(root, text='self-possessed', height=8)
antLabel1.grid(row=4, column=1)

showMeaningButton = Button(root, text="Show meaning...", command=press_show_meaning)
showMeaningButton.grid(row=5, column=0)

nextWordButton = Button(root, text="Next word", command=press_next_word)
nextWordButton.grid(row=5, column=1)

root.mainloop()

'''
height=2,3,3,8,8
root.mainloop()
'''
