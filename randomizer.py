def replacer(phrase,toreplace):
    char = 0
    ret = ''
    try:
        while True:
            fish = phrase[char]
            if fish == toreplace:
                nothing = ''
            else:
                ret = ret + fish
            char += 1
    except:
        print('')
    return ret
        
from random import randint
inp = ''
fish = 'start'
while fish != '':
    print('\n'*50)
    printer = replacer(inp,',')
    printer = replacer(printer,'\'')
    printer = replacer(printer,']')
    printer = replacer(printer,'[')
    print('you have the following words in your list: ',printer)
    fish = input('enter an entry. if you are finished, press enter. :  ')
    inp = inp + '   .      ' + fish
word = inp.split()
long = (len(word))
while True:
    print('\n'*50)
    long = (len(word))
    rand = randint(0,long-1)
    w = word[rand]
    printer = str(word)
    printer.replace(',','')
    printer = replacer(word,'\'')
    printer = replacer(printer,']')
    printer = replacer(printer,'[')
    print('you have the following words in your list: ',printer)
    print('press enter to generate another entry. Press r to delete this entry\n\n')
    inpu = input(word[rand])
    if inpu == 'r':
        word = str(word)
        word = word.replace(w,'')
        word = replacer(word,'\'')
        word = word.replace(',')
        word = replacer(word,']')
        word = replacer(word,'[')
        word = word.split()
        
        
