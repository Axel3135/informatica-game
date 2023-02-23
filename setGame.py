
'''Hier komt alle logic voor het spel set.
    het moet in ieder geval een card en game class hebben
    in de card class moeten in ieder geval het plaatje en de waardes van de kaart staan.
    in de game class moet er in ieder geval een deck gemaakt worden waar random kaarten uit kunnen worden getrokken.
    mogelijk een player class die kaarten, punten, highscore, etc per speler bijhoudt.
    '''
from random import shuffle

class SetGame:
    def __init__(self):
        self.fillDeck()
        self.shuffle()
        print(self.cards)
        print(len(self.cards))

    def fillDeck(self):
        amounts = range(3)
        colours = ["red", "green", "purple"]
        patterns = ["empty", "striped", "fill"]
        shapes = ["pill", "wave", "diamond"]
        self.cards = [SetCard(i, j, k, l) for i in amounts for j in colours for k in patterns for l in shapes]  # maakt een deck met alle 81 verschillende kaarten

    def shuffle(self):
        shuffle(self.cards)

    def isSet(self, card1, card2, card3):
        if ((card1.amount == card2.amount and card2.amount == card3.amount) or (card1.amount != card2.amount and card2.amount != card3.amount and card3.amount != card1.amount)):
            if ((card1.colour == card2.colour and card2.colour == card3.colour) or (card1.colour != card2.colour and card2.colour != card3.colour and card3.colour != card1.colour)):
                if ((card1.pattern == card2.pattern and card2.pattern == card3.pattern) or (card1.pattern != card2.pattern and card2.pattern != card3.pattern and card3.pattern != card1.pattern)):
                    if ((card1.shape == card2.shape and card2.shape == card3.shape) or (card1.shape != card2.shape and card2.shape != card3.shape and card3.shape != card1.shape)):
                        return True  # als alles hetzelfde of verschillend is, is het goed.
        return False





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


class Player:
    def __init__(self):
        pass
a1 = SetCard(0, "red", "empty", "wave")
a2 = SetCard(0, "green", "striped", "diamond")
a3 = SetCard(0, "purple", "fill", "pill")
print(a1.pattern)
b = SetGame()
print(b.isSet(a1, a2, a3))