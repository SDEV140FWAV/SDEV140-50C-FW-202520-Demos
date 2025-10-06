from card import Card, Deck

class Pile:
    def __init__(self):
        self.cards = []

    def playCard(self, card:Card):
        self.cards.append(card)
        return True
    
    def getTopCard(self):
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)
    
    def __str__(self): 
        output = ""
        for card in self.cards:
            output += str(card) + "\n"
        return output

class FoundPile(Pile):
    def __init__(self, num):
        Pile.__init__(self)
        if num < 1 or num > 4:
            raise ValueError(f"Sequence Num {num} is invalid")
        self.num = num
        self.sequence = []
        for i in range(13):
            self.sequence.append(Card.RANKS[(((i+1)*self.num) - 1) % 13])
    
    def playCard(self, card:Card):
        if card.rank == self.sequence[len(self.cards)]:
            self.cards.append(card)
            return True
        else:
            return False
    
    def __str__(self):
        return str(self.cards[len(self.cards) - 1])
    

class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.foundations = []
        self.wastes = []
        for i in range(1,5):
            self.foundations.append(FoundPile(i))
            self.wastes.append(Pile())
        self.foundationSetup()
        self.card_to_play = None
    
    def foundationSetup(self):
        needA = True
        need2 = True
        need3 = True
        need4 = True
        for card in self.deck.cards:
            if card.rank.upper() == 'A' and needA:
                self.deck.cards.remove(card)
                self.foundations[0].playCard(card)
                needA = False
            elif card.rank.upper() == "2" and need2:
                self.deck.cards.remove(card)
                self.foundations[1].playCard(card)
                need2 = False
            elif card.rank.upper() == "3" and need3:
                self.deck.cards.remove(card)
                self.foundations[2].playCard(card)
                need3 = False
            elif card.rank.upper() == "4" and need4:
                self.deck.cards.remove(card)
                self.foundations[3].playCard(card)
                need4 = False
            if not needA and not need2 and not need3 and not need4:
                break

    def drawCard(self):
        if len(self.deck) == 0:
            raise RuntimeError("Deck is empty")
        if self.card_to_play == None:
            self.card_to_play = self.deck.deal()

    def calculateScore(self):
        score = 0
        score += len(self.deck)
        for pile in self.wastes:
            score += len(pile)
        return score
    
    def finished(self):
        return self.card_to_play == None and len(self.deck) == 0
    
    def playDrawnCard(self, pile_num, destination="foundation"):
        if self.card_to_play == None:
            raise RuntimeError("Invalid Move: No Drawn Card")
        if destination == "foundation":
            if self.foundations[pile_num].playCard(self.card_to_play):
                self.card_to_play = None
            else:
                raise RuntimeError(f"Invalid Move: The next card for foundation #{pile_num + 1} is {self.foundations[pile_num].sequence[len(self.foundations[pile_num])]}")
        else:
            self.wastes[pile_num].playCard(self.card_to_play)
            self.card_to_play = None

    def playWasteCard(self,waste_num, found_num):
        if len(self.wastes[waste_num]) == 0:
            raise RuntimeError("Invalid Move: Waste Pile is Empty")
        card = self.wastes[waste_num].getTopCard()
        if not self.foundations[found_num].playCard(card):
            self.wastes[waste_num].playCard(card)
            raise RuntimeError(f"Invalid Move: The next card for foundation #{found_num + 1} is {self.foundations[found_num].sequence[len(self.foundations[found_num])]}")
    def wastePlay(self):
        for waste in self.wastes:
            if len(waste) > 0:
                return True
        return False

