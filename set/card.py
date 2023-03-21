

class Card:
    def __init__(self,name,color,shape,number,shade):
        self.color = color
        self.shape = shape
        self.number = number
        self.shade = shade
        self.clicked = False

    def clicked(self, card_name):
        self.clicked = not self.clicked


    def decode(self, image):
        '''Deze functie moet van de image die hij krijgt de code waarmee hij genoemd is omzetten naar kleuren en zo een nieuwe kaart maken (moet in een andere Class)'''
        pass