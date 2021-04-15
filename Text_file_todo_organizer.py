while True:
    print('\n'*50)
    print('current list below')
    File_object = open("copy.txt","r+")
    listy = (File_object.read(10000))
    print(listy)
    command = input('enter the command \n  > ')
    command = command + '     ' 
    line = command[0] + command[1] + command[2]
    command = command.replace(line,' ')
    if line == 'add':
        fish = command
        fish = '\n' + fish
        File_object = open("copy.txt","a")
        File_object.writelines(fish)
    if line == 'del':
        fish = command
        if 'all' in fish:
            listy = ''
        else:
            if fish in listy:
                listy = listy.replace(fish,'')
        File_object = open("copy.txt","w")
        File_object.write(listy)
