while True:
    command = input('enter "yes" or "no": ')
    if command == 'yes':
        print(n, f'{n} > 0' , n > 0)
        n -= 1
    elif command == "no":
        print(' stop.')
    else:
        print('wrong command') 