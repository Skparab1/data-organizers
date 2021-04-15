phrase = input('enter your phrase')
cwithspaces = len(phrase)
words = 0
char = 0
try:
    while True:
        fish = phrase[char]
        if fish == ' ':
            words += 1
        char += 1
except:
    print('')
letters = 0
char = 0
try:
    while True:
        fish = phrase[char]
        if fish != ' ':
            letters += 1
        char += 1
except:
    print('')
print('The number of words are: ', words)
print('The number of characters with spaces are: ', cwithspaces)
print('The number of characters without spaces are: ',letters) 