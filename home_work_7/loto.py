#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random


class Card:

    def zeros_change(self, row, number_of_zeros):
        set_1 = set(random.choices(row, k=number_of_zeros))
        while len(set_1) < number_of_zeros:
            set_1.add(random.choice(row))
        for num in range(len(row)):
            if row[num] in set_1:
                row[num] = 0
        return row

    def __init__(self, player_name):
        self._player_name = player_name
        self._list_of_card = random.sample(range(1, 91), 27)
        self._row_1 = sorted(self._list_of_card[:9])
        self._row_2 = sorted(self._list_of_card[9:18])
        self._row_3 = sorted(self._list_of_card[18:])
        for row in (self._row_1, self._row_2, self._row_3):
            self.zeros_change(row, 4)
        self._list_of_card = self._row_1 + self._row_2 + self._row_3

    def beautiful_card(self, row):
        beautiful_row = ''
        for num in row:
            if num == 0:
                beautiful_row += '{:<3}'.format(' ')
            else:
                beautiful_row += '{:<3}'.format(num)
        return beautiful_row

    def crossing(self, num):
        for iter in range(len(self._list_of_card)):
            if num == self._list_of_card[iter]:
                self._list_of_card[iter] = '-'
        self._row_1 = self._list_of_card[:9]
        self._row_2 = self._list_of_card[9:18]
        self._row_3 = self._list_of_card[18:]

    def __str__(self):
        return '{}\n {}\n {}\n {}'.format(self._player_name, self.beautiful_card(self._row_1),
        self.beautiful_card(self._row_2), self.beautiful_card(self._row_3))


myCard = Card("Моя карточка")
compCard = Card("Карточка компьютера")
print(myCard)
print(compCard)


def game():
    lottery_dram = [num for num in range(1, 91)]
    throw = 0
    game_over = False
    while not game_over:
        throw += 1
        num = random.choice(lottery_dram)
        print('Ход {}, число {}'.format(throw, num))
        cont = input("Зачеркнуть? y/n ")
        if (cont == 'y' and num in set(myCard._list_of_card)) or (cont == 'n' and num not in set(myCard._list_of_card)):
            game_over = False
        else:
            print("Вы проиграли")
            game_over = True
            return 'Ну ты и лох невнимательный!'
        for card in (myCard, compCard):
            card.crossing(num)
        print(myCard)
        print(compCard)
        lottery_dram.remove(num)
        print('Осталось ходов: ', len(lottery_dram))
        if myCard._list_of_card.count('-') == 15:
            print("Вы выиграли")
            game_over = True
        elif compCard._list_of_card.count('-') == 15:
            print("Вы проиграли")
            game_over = True
        else:
            game_over = False
        if game_over:
            print("Невыпавшие бочонки: ", lottery_dram)
            return 'Игра окончена'


print(game())





