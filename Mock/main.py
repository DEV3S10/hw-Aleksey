import re

with open('MOCK_DATA.txt', 'r') as file:
    content = file.read()


def read_names():
    names = re.findall(r'([A-Z][A-Za-z-\']+)\s([A-Z][A-Za-z-\']+)', content)  #|([A-Z]([a-z])+\s([a-z]+)\s[A-Z][a-z]+)  - for 3 names
    c = 0
    with open('names.txt', 'w') as f:
        for i in names:
            c += 1
            f.write(f'{c}. {i}\n')
    b = 0
    print(f'list of persons:')
    for i in names:
        b += 1
        print(f'{b}. {i}')


def read_emails():
    emails = re.findall(r'[A-Za-z0-9_-]+@[a-z.0-9]+', content)
    c = 0
    with open('emails.txt', 'w') as f:
        for i in emails:
            c += 1
            f.write(f'{c}. %s\n' % i)
    c = 0
    print('List of emails:')
    for i in emails:
        c += 1
        print(f'{c}. {i}')


def read_names_of_files():
    names_of_files = re.findall(r'\s([A-Za-z0-9]+\.[A-Za-z0-9]{1,4})', content)
    b = 0
    with open('names_of_files.txt', 'w') as f:
        for i in names_of_files:
            b += 1
            f.write(f'{b}. %s\n' % i)
    c = 0
    print('Names of files:')
    for i in names_of_files:
        c += 1
        print(f'{c}. {i}')


def read_codes_of_colors():
    codes = re.findall(r'\s#([a-z0-9]{6})\b', content)
    b = 0
    with open('codes_of_colors.txt', 'w') as f:
        for i in codes:
            b += 1
            f.write(f'{b}. %s\n' % i)
    c = 0
    print('Codes of colors:')
    for i in codes:
        c += 1
        print(f'{c}. {i}')
