choice = 'hi'
entry_number = 0
entry_number1 = ''
entry_number2 = ''
entry_number3 = ''
entry_number4 = ''
entry_number5 = ''
entry_number6 = ''
entry_number7 = ''
entry_number8 = ''
entry_number9 = ''
entry_number10 = ''
entry_number11 = ''
while True:
    print('\n' * 50)
    print('welcome to the database')
    print('press c to create a new entry')
    print('press d to delete an entry')
    print('press v to view an entry')
    print('press e to edit an entry')
    print('press s to search the database')
    choice = input('enter you choice followed by enter')
    if choice == 'c':
        print('\n' * 50)
        entry_number += 1
        name = input('please enter entry name ')
        print('\n' * 50)
        if entry_number == 1:
            entry_number1 = ('1.' + name)
            content_number1 = input('enter ' + entry_number1 + '\'s contents ')
        if entry_number == 2:
            entry_number2 = ('2.' + name)
            content_number2 = input('enter '+ entry_number2 + '\'s contents ')
        if entry_number == 3:
            entry_number3 = ('3.' + name)
            content_number3 = input('enter '+ entry_number3 + '\'s contents ')
        if entry_number == 4:
            entry_number4 = ('4.' + name)
            content_number4 = input('enter '+ entry_number4 + '\'s contents ')
        if entry_number == 5:
            entry_number5 = ('5.' + name)
            content_number5 = input('enter '+ entry_number5 + '\'s contents ')
        if entry_number == 6:
            entry_number6 = ('6.' + name)
            content_number6 = input('enter '+ entry_number6 + '\'s contents ')
        if entry_number == 7:
            entry_number7 = ('7.' + name)
            content_number7 = input('enter '+ entry_number7 + '\'s contents ')
        if entry_number == 8:
            entry_number8 = ('8.' + name)
            content_number8 = input('enter '+ entry_number8 + '\'s contents ')
        if entry_number == 9:
            entry_number9 = ('9.' + name)
            content_number9 = input('enter '+ entry_number9 + '\'s contents ')
        if entry_number == 10:
            entry_number10 = ('10.' + name)
            content_number10 = input('enter '+ entry_number10 + '\'s contents ')
        if entry_number == 11:
            entry_number11 = ('11.' + name)
            content_number11 = input('enter '+ entry_number11 + '\'s contents ')
        if entry_number >= 12:
            print('The database is out of memory. please delete an entry')
        input('your entry has been saved')
    if choice == 'd':
        print('\n' * 50)
        print(entry_number1,'\n',entry_number2,'\n',entry_number3,'\n',entry_number4,'\n',entry_number5,'\n',entry_number6,'\n',entry_number7,'\n',entry_number8,'\n',entry_number9,'\n',entry_number10,'\n',entry_number11,'\n')
        deleter = input('enter the number of the entry to be deleted')
        if deleter == '1':
            content_number1 = ''
            entry_number1 = ''
        if deleter == '2':
            content_number2 = ''
            entry_number2 = ''
        if deleter == '3':
            content_number3 = ''
            entry_number3 = ''
        if deleter == '4':
            content_number4 = ''
            entry_number4 = ''
        if deleter == '5':
            content_number5 = ''
            entry_number5 = ''
        if deleter == '6':
            content_number6 = ''
            entry_number6 = ''
        if deleter == '7':
            content_number7 = ''
            entry_number7 = ''
        if deleter == '8':
            content_number8 = ''
            entry_number8 = ''
        if deleter == '9':
            content_number9 = ''
            entry_number9 = ''
        if deleter == '10':
            content_number10 = ''
            entry_number10 = ''
        if deleter == '11':
            content_number11 = ''
            entry_number11 = ''
    if choice == 'v' :
        print('\n' * 50)
        print(entry_number1,'\n',entry_number2,'\n',entry_number3,'\n',entry_number4,'\n',entry_number5,'\n',entry_number6,'\n',entry_number7,'\n',entry_number8,'\n',entry_number9,'\n',entry_number10,'\n',entry_number11,'\n')
        viewer = input('enter the number of the entry to be viewed')
        print('\n' * 50)
        if viewer == '1':
            print(content_number1)
        if viewer == '2':
            print(content_number2)
        if viewer == '3':
            print(content_number3)
        if viewer == '4':
            print(content_number4)
        if viewer == '5':
            print(content_number5)
        if viewer == '6':
            print(content_number6)
        if viewer == '7':
            print(content_number7)
        if viewer == '8':
            print(content_number8)
        if viewer == '9':
            print(content_number9)
        if viewer == '10':
            print(content_number10)
        if viewer == '11':
            print(content_number11)
        input()
    if choice == 'e':
        print('\n' * 50)
        print(entry_number1,'\n',entry_number2,'\n',entry_number3,'\n',entry_number4,'\n',entry_number5,'\n',entry_number6,'\n',entry_number7,'\n',entry_number8,'\n',entry_number9,'\n',entry_number10,'\n',entry_number11,'\n')
        editor = input('enter the number of the entry to be edited')
        print('\n' * 50)
        if editor == '1':
            print('type to add text')
            content_number1 += input(content_number1)
        if editor == '2':
            print('type to add text')
            content_number2 += input(content_number2)
        if editor == '3':
            print('type to add text')
            content_number3 += input(content_number3)
        if editor == '4':
            print('type to add text')
            content_number4 += input(content_number4)
        if editor == '5':
            print('type to add text')
            content_number5 += input(content_number5)
        if editor == '6':
            print('type to add text')
            content_number6 += input(content_number6)
        if editor == '7':
            print('type to add text')
            content_number7 += input(content_number7)
        if editor == '8':
            print('type to add text')
            content_number8 += input(content_number8)
        if editor == '9':
            print('type to add text')
            content_number9 += input(content_number9)
        if editor == '10':
            print('type to add text')
            content_number10 += input(content_number10)
        if editor == '11':
            print('type to add text')
            content_number11 += input(content_number11)
    if choice == 's':
        text_to_find = input('enter search keywords')
        if text_to_find in content_number1:
            print('the text has been found in' , entry_number1)
            print(content_number1)
        elif text_to_find in content_number2:
            print('the text has been found in' , entry_number2)
            print(content_number2)
        elif text_to_find in content_number3:
            print('the text has been found in' , entry_number3)
            print(content_number3)
        elif text_to_find in content_number4:
            print('the text has been found in' , entry_number4)
            print(content_number4)
        elif text_to_find in content_number5:
            print('the text has been found in' , entry_number5)
            print(content_number5)
        elif text_to_find in content_number6:
            print('the text has been found in' , entry_number6)
            print(content_number6)
        elif text_to_find in content_number7:
            print('the text has been found in' , entry_number7)
            print(content_number7)
        elif text_to_find in content_number8:
            print('the text has been found in' , entry_number8)
            print(content_number8)
        elif text_to_find in content_number9:
            print('the text has been found in' , entry_number9)
            print(content_number9)
        elif text_to_find in content_number11:
            print('the text has been found in' , entry_number11)
            print(content_number11)
        else:
            print('the keyword was not found')
        input('')
        
       
            
            
            
       