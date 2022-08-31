import main

answer = 0
while True:
    answer = int(input('\nChoose an option:\n'
          '1 - read names of persons\n'
          '2 - read emails of persons\n'
          '3 - read names of files\n'
          '4 - read codes of colors\n'
          '5 - exit\n'
          'enter your choise: '))

    if answer == 1:
        main.read_names()

    elif answer == 2:
        main.read_emails()

    elif answer == 3:
        main.read_names_of_files()

    elif answer == 4:
        main.read_codes_of_colors()

    elif answer == 5:
        print(f'bye...')
        break

    else:
        print('Нормально пиши')
