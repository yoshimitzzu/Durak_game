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

    def gen_cards(self):
        # раздает карты, не больше 6 в начальной руке. выход: два списка с уникальными картами у каждого игрока

        self.player_cards = []
        for card in range(6):
            player_card = random.choice(self.cards)
            self.player_cards.append(player_card)  # добавляет в список игрока(в руку игрока) карту
            self.cards.remove(player_card)  # удаляет из общего числа карт сгенерированную карту

        self.comp_cards = []
        for card in range(6):
            comp_card = random.choice(self.cards)
            self.comp_cards.append(comp_card)  # как и у игрока
            self.cards.remove(comp_card)

        print('Ваши карты: ', list((item[0] for item in self.player_cards))), print('Карты помпьютера: ', list(
            (item[0] for item in self.comp_cards))), print('Козырь: ', self.get_mast(Durak, self.kozyr[0]))

        return self.player_cards, self.comp_cards

    def gen_kozyr_list(self):  # пересоздает список с картами, имеющие масть козыря, изменяя силу карт
        kozyr_card = random.choice(self.cards)
        self.kozyr = kozyr_card
        new_list = self.kozyr[0].rsplit('_')
        self.mast_kozyr = new_list[1]
        for card in self.cards:
            if self.mast_kozyr in card[0]:
                card[1] = card[1] + 9
        return self.cards

    def get_mast(self, card):  # узнает масть карты
        new_list = card.rsplit('_')
        self.mast = new_list[1]
        return self.mast

    def whos_first_turn(self):
        player_smallest_card = min(item[1] for item in self.player_cards)
        # цикл перебора вторых элементов подсписков(силы)
        comp_smallest_card = min(item[1] for item in self.comp_cards)
        if player_smallest_card < comp_smallest_card:
            self.turn = True
            self.player_turn(Durak)
        else:
            self.turn = False
            self.comp_turn(Durak)

    def game_start(self):
        self.table = []
        self.gen_kozyr_list(Durak)
        self.gen_cards(Durak)
        self.whos_first_turn(Durak)