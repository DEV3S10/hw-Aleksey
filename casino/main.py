import os
import random
from envparse import env


class Casino:
    def __init__(self):
        self.__cash = int(os.environ.get('MY_MONEY'))

        while int(self.__cash) > 0:
            print(f"Ваш денги: {self.__cash}")
            self.__win_slot = random.randint(1, 30)
            print(self.__win_slot)
            self.__slot = int(30)
            self.__bet = int(input('Сделайте ставку: '))
            if self.__bet > self.__cash:
                print("У вас недостаточно денег! ")
            else:
                self.__choice = int(input('Выберите слот: '))
                if self.__choice > self.__slot:
                    print("Выберите слота только от 1-30")
                    userRound = input('Хотите ешё поиграть?("да" или "нет"')
                    if userRound == 'да':
                        continue
                    elif userRound == 'нет':
                        break
                    else:
                        print("да или нет?")

    @property
    def win(self):
        return self.__win_slot

    @win.setter
    def win(self, value):
        self.__win_slot = value

    @property
    def slot(self):
        return self.__slot

    @slot.setter
    def slot(self, value):
        self.__slot = value


env.read_envfile('settings.env')
