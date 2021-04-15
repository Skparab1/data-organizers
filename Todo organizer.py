import math
command = 'start'
todolist = ''
line = ''
addent = ''
default = 'clr'
command_status = 'Ready/Default'
recently_deleted = ''
while True :
    print('\n' * 2)
    print('your current list is \n' , todolist)
    print('\n' * 2)
    print('For a full list of commands run    -help')
    command = input('enter the command \n' + command_status + ' > ')
    command = command + '     ' 
    if default == 'clr':
        line = command[0] + command[1] + command[2] + command[3] + command[4]
        if line in command:
            command = command.replace(line,' ')
    else:
        command = ' ' + command
        if 'clr' in command:
            default = 'clr'
            command_status = 'Ready/Default'
        if 'del' in command:
            default = 'del'
            command_status = 'Ready/Del'
        if 'add' in command:
            default = 'add'
            command_status = 'Ready/Add'
        if 'rcv' in command:
            default = 'rcv'
            command_status = 'Ready/Recover'
    if line == '-add ' or default == 'add':
        todolist = todolist + '\n' + command
    if line == '-clr ' :
        print('\n' * 50)
    if line == '-del ' or default == 'del':
        if 'all' in command:
            recently_deleted = recently_deleted + '\n' + todolist
            todolist = ' '
        elif 'space' in command:
            if '  ' in todolist:
                todolist = todolist.replace('  ','')
        else:
            if command in todolist:
                todolist = todolist.replace(command,'')
                recently_deleted = recently_deleted + '\n' + command
    if line == '-mod ':
        if 'add' in command:
            default = 'add'
            command_status = 'Ready/Add'
        if 'del' in command:
            default = 'del'
            command_status = 'Ready/Del'
        if 'rcv' in command:
            default = 'rcv'
            command_status = 'Ready/Recover'
    if line == '-rcv ' or default == 'rcv' :
        if 'all' in command:
            todolist = todolist + recently_deleted
            recently_deleted = ' '
        else:
            if command in recently_deleted:
                recently_deleted = recently_deleted.replace(command,'')
                todolist = todolist + command + '\n'
            
        
    if line == '-help':
        print('   -add        to add event to list')
        print('   -clr        to clear screen')
        print('   -mod        to set a command mode')
        print('   -rcv        to recover a deleted list')
        input('   -del        to delete events from list')