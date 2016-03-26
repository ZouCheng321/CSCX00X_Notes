import pickle


with open('./vocabDatabaseFile.pkl', 'rb') as pickle_file:
    vocabulary = pickle.load(pickle_file)

print(vocabulary)

for i in vocabulary:
    if i[0].startswith('LO'):
        print(i)


