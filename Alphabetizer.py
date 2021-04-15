inp = ''
fish = 'start'
while fish != '':
    print('\n'*50)
    print('you have the following words in your list: ',inp)
    fish = input('enter an entry. if you are finished, press enter. :  ')
    inp = inp + ' ' + fish
word = inp.split()
word.sort()
word = str(word)
char = 0
ret = ''
try:
    while True:
        fish = word[char]
        if fish == '\'':
            nothing = ''
        else:
            ret = ret + fish
        char += 1
except:
    print('')
new = ''
char = 0
try:
    while True:
        fish = ret[char]
        if fish == ',':
            nothing = ''
        else:
            new = new + fish
        char += 1
except:
    print('')
final = ''
char = 0
try:
    while True:
        fish = new[char]
        if fish == '[':
            nothing = ''
        else:
            final = final + fish
        char += 1
except:
    print('')
toprint = ''
char = 0
try:
    while True:
        fish = final[char]
        if fish == ']':
            nothing = ''
        else:
            toprint = toprint + fish
        char += 1
except:
    print('')
print(toprint)

    
    
    