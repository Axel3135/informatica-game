
'''Hier komt alle logic voor het spel set.
    het moet in ieder geval een card en game class hebben
    in de card class moeten in ieder geval het plaatje en de waardes van de kaart staan.
    in de game class moet er in ieder geval een deck gemaakt worden waar random kaarten uit kunnen worden getrokken.
    mogelijk een player class die kaarten, punten, highscore, etc per speler bijhoudt.
    '''
class SetGame:
    def __init__(self):
        pass

class SetCard:
    def __init__(self, amount, pattern, figure):
        '''class voor het beheren van één set kaart
        amount is een int van 0-2 die de hoeveelheid vormpjes op de kaart aangeeft
        pattern is een str uit patterns die het patroon aangeeft van de vormpjes 
        figure is een str uit figures die de vorm van de kaart aangeeft.
        '''
        patterns = {"empty":0, "striped":1, "fill":2}
        figures = {"pill":0, "wave":1, "diamond":2}
        self.amount = amount
        self.pattern = patterns[pattern]
        self.figure = figures[figure]


class Player:
    def __init__(self):
        pass
a = SetCard(0, 0, "wave")
print(a.pattern)