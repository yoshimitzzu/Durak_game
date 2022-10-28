from main import Durak
import pytest


class TestDurak:

    def setup(self):
        self.durak_game = Durak
        print('Test started')

    def teardown(self):
        print('Test finished')

    def test_cards_num(self):
        durak_game = Durak
        durak_game.all_cards(Durak)
        assert len(durak_game.cards) == 36

    def test_cards_in_hand(self):
        durak_game = Durak
        durak_game.gen_kozyr_list(Durak)
        durak_game.gen_cards(Durak)
        assert len(durak_game.player_cards) == 6
        assert len(durak_game.comp_cards) == 6

    def test_similar_cards(self):
        durak_game = Durak
        durak_game.gen_kozyr_list(Durak)
        durak_game.gen_cards(Durak)
        set_player = set({})
        set_comp = set({})
        for i in range(len(durak_game.player_cards)):
            set_player.add(durak_game.player_cards[i][0])

        for i in range(len(durak_game.comp_cards)):
            set_player.add(durak_game.comp_cards[i][0])

        assert set_player.isdisjoint(set_comp) == True
