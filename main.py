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

    def comp_turn(self):
        if len(self.comp_cards) > 0 and len(self.player_cards) > 0 and self.turn == False and len(self.table) == 0:
            # выполняется, если начинает ходить компьютер
            print('--------Ход компьютера--------')
            tmp_card = random.choice(self.comp_cards)
            self.table.append(tmp_card)
            self.comp_cards.remove(tmp_card)
            print('На столе: ', self.table[0][0])
            self.player_turn(Durak)

        else:
            c_avble_cards_to_beat = []  # список с картами из руки, которыми можно побить
            changed_table = []  # список [[масть, сила].....[масть, сила]...]
            changed_table = copy.deepcopy(self.table)
            for i in range(len(changed_table)):
                changed_table[i][0] = self.get_mast(Durak, changed_table[i][0])

            for i in range(len(self.comp_cards)):
                if (self.get_mast(Durak, self.comp_cards[i][0]) == changed_table[0][0] or self.get_mast(Durak,
                                                                                                        self.comp_cards[
                                                                                                            i][
                                                                                                            0]) == self.mast_kozyr) and \
                        self.comp_cards[i][1] > changed_table[0][1] and len(self.table) == 1:
                    c_avble_cards_to_beat.append(self.comp_cards[i])
                    # создается список с картами, которыми комп может побить

            if len(c_avble_cards_to_beat) > 0:
                self.beat_cards = []  # список карт, которыми побили
                card_to_beat = random.choice(c_avble_cards_to_beat)
                self.beat_cards.append(card_to_beat)
                self.comp_cards.remove(card_to_beat)
                print('Карты, которыми побили ', self.beat_cards[0][0])
                print('На столе               ', self.table[0][0])
                self.table.clear()
                self.turn = False
                self.comp_turn(Durak)


            elif len(c_avble_cards_to_beat) == 0 and self.turn:
                # если список с доступными картами пустой, то компьютер берет карту
                print('Компьютер берет карту ')
                self.comp_cards.append(self.table[0])
                self.table.remove(self.table[0])
                self.turn = True
                self.player_turn(Durak)

    def player_turn(self):
        if len(self.comp_cards) > 0 and len(self.player_cards) > 0 and self.turn and len(self.table) == 0:
            print("-------Ваш ход-------")
            print('Ваши карты', list((item[0] for item in self.player_cards)))
            bool_card = ""
            while not bool_card:
                tmp_card = str(input('Выберите карту '))
                for card in self.player_cards:
                    if tmp_card == card[0]:
                        tmp_card = card
                        bool_card = tmp_card
                        self.table.append(tmp_card)
                        self.player_cards.remove(card)
                        print('На столе: ', self.table[0][0])
                        print('Ваши карты: ', list((item[0] for item in self.player_cards))), \
                        print('Карты помпьютера: ', list((item[0] for item in self.comp_cards)))
            self.comp_turn(Durak)

        elif len(self.player_cards) > 0 and self.turn == False and len(self.table) != 0:
            avble_player_cards = []  # список с картами из руки, которыми можно побить
            changed_table = []  # список [[масть, сила].....[масть, сила]...]
            changed_table = copy.deepcopy(self.table)
            for i in range(len(changed_table)):
                changed_table[i][0] = self.get_mast(Durak, changed_table[i][0])

            for i in range(len(self.player_cards)):
                if (self.get_mast(Durak, self.player_cards[i][0]) == changed_table[0][0] or self.get_mast(Durak,
                                                                                                          self.player_cards[
                                                                                                              i][
                                                                                                              0]) == self.mast_kozyr) and \
                        self.player_cards[i][1] > changed_table[0][1] and len(self.table) == 1:
                    avble_player_cards.append(self.player_cards[i])
            print('Доступные карты: ', list((item[0] for item in avble_player_cards)))

            if not avble_player_cards and self.turn == False:
                self.beat_cards = []
                print('Вы берете карту')
                self.player_cards.append(self.table[0])
                self.table.clear()
                print('Ваши карты', list((item[0] for item in self.player_cards)))
                self.turn = False
                self.comp_turn(Durak)

            elif len(avble_player_cards) > 0 and self.turn == False:
                bool_card = ""
                self.beat_cards = []
                while not bool_card:
                    input_data = input('Выберите карту, которой хотите побить ')
                    for i in range(len(avble_player_cards)):
                        if input_data == avble_player_cards[i][0]:
                            bool_card = avble_player_cards[i]
                            self.beat_cards.append(avble_player_cards[i])
                            self.player_cards.remove(avble_player_cards[i])
                            print('Карты, которыми побили ', self.beat_cards[0][0])
                            print('На столе               ', self.table[0][0])
                            self.table.clear()
                            avble_player_cards.clear()
                            break
                self.turn = True
                self.player_turn(Durak)


Durak.all_cards(Durak)
Durak.game_start(Durak)