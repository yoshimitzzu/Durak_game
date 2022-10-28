import random
import copy
import re


class Durak:
    def __init__(self):  # инициализатор класса
        self.table = []


    def all_cards(self):  # генерирует все существующие карты в колоде. выход: целая колода (36 карт)
        self.card_type = [['6', 1], ['7', 2], ['8', 3], ['9', 4], ['10', 5], ['valet', 6], ['dama', 7], ['korol', 8],
                          ['tuz', 9]]  # self.card_type[i][1] - "сила" карты

        self.spades = copy.deepcopy(self.card_type)
        for i in range(len(self.spades)):
            self.spades[i][0] = self.spades[i][0] + '_piki'

        self.club = copy.deepcopy(self.card_type)
        for i in range(len(self.club)):
            self.club[i][0] = self.club[i][0] + '_kresti'

        self.hearts = copy.deepcopy(self.card_type)
        for i in range(len(self.hearts)):
            self.hearts[i][0] = self.hearts[i][0] + '_chervi'

        self.diamonds = copy.deepcopy(self.card_type)
        for i in range(len(self.diamonds)):
            self.diamonds[i][0] = self.diamonds[i][0] + '_bubi'

        self.cards = self.spades + self.club + self.hearts + self.diamonds
        random.shuffle(self.cards)
        return self.cards