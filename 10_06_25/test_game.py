from game import Pile, FoundPile, Game
from card import Card, Deck

import pytest

def test_pile_sequence():
    pile = Pile()
    with pytest.raises(AttributeError):
        pile.sequence
    found1 = FoundPile(1)
    assert found1.sequence == ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    found2 = FoundPile(2)
    assert found2.sequence == ['2', '4', '6', '8', '10', 'Q', 'A', '3', '5', '7', '9', 'J', 'K']
    found3 = FoundPile(3)
    assert found3.sequence == ['3', '6', '9', 'Q', '2', '5', '8', 'J', 'A', '4', '7','10', 'K']
    found4 = FoundPile(4)
    assert found4.sequence == ['4', '8', 'Q', '3', '7', 'J', '2', '6', '10', 'A', '5', '9', 'K']

def test_game_setup():
    deck = Deck()
    assert len(deck) == 52
    game = Game()
    assert len(game.deck) == 48
    start_rank = ["A", "2", '3', "4"]
    for i in range(4):
        assert len(game.foundations[i]) == 1
        assert len(game.wastes[i]) == 0
        assert game.foundations[i].cards[0].rank == start_rank[i]
    assert game.card_to_play == None

def test_game_drawCard():
    game = Game()
    game.drawCard()
    assert len(game.deck) == 47
    assert game.card_to_play != None
    card = game.card_to_play
    game.drawCard()
    assert len(game.deck) == 47
    assert game.card_to_play == card

def test_game_drawAllCards():
    game = Game()
    for i in range(50):
        try:
            game.drawCard()
            game.card_to_play = None
        except RuntimeError as e:
            assert str(e) == "Deck is empty"
            break
    assert len(game.deck) == 0

def test_game_playCard():
    game = Game()
    card1 = Card("HEARTS", '3')
    card2 = Card("CLUBS", "2")
    card3 = Card("SPADES", "6")
    card4 = Card("Diamonds", "8")
    card5 = Card('hearts', "4")
    game.card_to_play = card1
    try:
        game.playDrawnCard(0)
    except RuntimeError:
        assert True
    else:
        assert False
    
    try:
        game.playDrawnCard(1)
    except RuntimeError:
        assert True
    else:
        assert False
    
    try:
        game.playDrawnCard(2)
    except RuntimeError:
        assert True
    else:
        assert False
    
    try:
        game.playDrawnCard(3)
    except RuntimeError:
        assert True
    else:
        assert False
    
    game.playDrawnCard(0,"waste")
    assert game.card_to_play == None
    assert len(game.wastes[0]) == 1

    game.card_to_play = card2
    game.playDrawnCard(0)
    assert game.card_to_play == None
    assert len(game.foundations[0]) == 2

    game.card_to_play = card5
    game.playDrawnCard(1)
    assert game.card_to_play == None
    assert len(game.foundations[1]) == 2

    game.card_to_play = card3
    game.playDrawnCard(2)
    assert game.card_to_play == None
    assert len(game.foundations[2]) == 2

    game.card_to_play = card4
    game.playDrawnCard(3)
    assert game.card_to_play == None
    assert len(game.foundations[3]) == 2

    try:
        game.playWasteCard(0,1)
    except RuntimeError:
        pass
    else:
        assert False

    try:
        game.playWasteCard(0,2)
    except RuntimeError:
        pass
    else:
        assert False

    try:
        game.playWasteCard(0,3)
    except RuntimeError:
        pass
    else:
        assert False
    
    try:
        game.playWasteCard(1,0)
    except RuntimeError:
        pass
    else:
        assert False
    
    game.playWasteCard(0,0)
    assert len(game.foundations[0]) == 3
    assert len(game.wastes[0]) == 0


def test_game_calculateScore():
    game = Game()
    assert game.calculateScore() == 48

    for i in range(4):
        game.drawCard()
        game.playDrawnCard(0, "waste")
    assert game.calculateScore() == 48
