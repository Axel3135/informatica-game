
'''Hier komt alle logic voor het spel set.
    het moet in ieder geval een card en game class hebben
    in de card class moeten in ieder geval het plaatje en de waardes van de kaart staan.
    in de game class moet er in ieder geval een deck gemaakt worden waar random kaarten uit kunnen worden getrokken.
    mogelijk een player class die kaarten, punten, highscore, etc per speler bijhoudt.
    '''
from random import shuffle

class SetGame:
    def __init__(self):
        self.deck = self.fillDeck()
        self.shuffle()
        self.active_cards = list()
        self.addCards(81)

        print(self.active_cards)
        print(f"active: {len(self.active_cards)}")
        print(len(self.deck))

    def fillDeck(self):
        amounts = range(3)
        colours = ["red", "green", "purple"]
        patterns = ["empty", "striped", "fill"]
        shapes = ["pill", "wave", "diamond"]
        return [SetCard(i, j, k, l) for i in amounts for j in colours for k in patterns for l in shapes]  # maakt een deck met alle 81 verschillende kaarten

    def shuffle(self):
        shuffle(self.deck)
    
    def addCards(self, amount):
        '''function that ads [amount] cards to the active cards'''
        self.active_cards.extend([self.deck[i] for i in range(amount)])
        del self.deck[0:amount]

    def isSet(self, card1, card2, card3):
        '''funcition for checking if a set of three cards is a valid set or not.
        '''
        if ((card1.amount == card2.amount and card2.amount == card3.amount) or (card1.amount != card2.amount and card2.amount != card3.amount and card3.amount != card1.amount)):
            if ((card1.colour == card2.colour and card2.colour == card3.colour) or (card1.colour != card2.colour and card2.colour != card3.colour and card3.colour != card1.colour)):
                if ((card1.pattern == card2.pattern and card2.pattern == card3.pattern) or (card1.pattern != card2.pattern and card2.pattern != card3.pattern and card3.pattern != card1.pattern)):
                    if ((card1.shape == card2.shape and card2.shape == card3.shape) or (card1.shape != card2.shape and card2.shape != card3.shape and card3.shape != card1.shape)):
                        return True  # als alles hetzelfde of verschillend is, is het goed.
        return False
    
    def checkForSet(self):
        '''function that checks for sets in the current active cards
        '''
        sets = list()
        for i in self.active_cards[0:-2]:
            for j in self.active_cards[self.active_cards.index(i)+1:-1]:
                for k in self.active_cards[self.active_cards.index(j)+1:]:# checkt alle combinaties van kaarten (zonder list indexes, zouden permutaties gecheckt worden.)
                    # print(self.active_cards.index(i), self.active_cards.index(j), self.active_cards.index(k))
                    if (not (i==j or j==k or k==i)):
                        if self.isSet(i, j, k):
                            sets.append([i, j, k])
        return sets

class SetCard:
    def __init__(self, amount, colour, pattern, shape):
        '''class voor het beheren van één set kaart
        amount is een int van 0-2 die de hoeveelheid vormpjes op de kaart aangeeft
        pattern is een str uit patterns die het patroon aangeeft van de vormpjes 
        figure is een str uit figures die de vorm van de kaart aangeeft.
        '''
        colours = {"red":0, "green":1, "purple":2}
        patterns = {"empty":0, "striped":1, "fill":2}
        shapes = {"pill":0, "wave":1, "diamond":2}
        self.amount = amount
        self.colour = colours[colour]
        self.pattern = patterns[pattern]
        self.shape = shapes[shape]
        self.image = f"{amount}_{colour}_{pattern}_{shape}.png"
        self.properties = [self.amount, self.colour, self.pattern, self.shape]


class Player:
    def __init__(self):
        pass
a1 = SetCard(0, "red", "empty", "wave")
a2 = SetCard(0, "green", "striped", "diamond")
a3 = SetCard(0, "purple", "fill", "pill")
print(a1.pattern)
b = SetGame()
bsets = b.checkForSet()
for i in bsets:
    print(f"\nset: {bsets.index(i)}")
    for j in i:
        print(j.properties)
print(b.isSet(a1, a2, a3))