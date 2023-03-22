'''code voor het spel vier op een rij'''

class Board():
    def __init__(self):
        self.height = 7
        self.width = 8
        self.board = [[None for i in range(self.width)] for j in range(self.height)]
        print(self.board)

    def placeDisk(self, index, colour):
        '''functie die disks plaatst in het board van boven naar beneden (andersom dan zou moeten dus.)
        index is de list index van de kolom waarin de schijf geplaatst wordt
        colour is de kleur van de schijf, hier moet nog algemene notatie voor komen
        '''
        for i in self.board:
            if i[index] == None:
                i[index] = colour
                return True
        return False
    
    def checkBoard(self, symbol):
        '''Checkt het bord voor 4 op een rij
        hij checkt eerst alle horizontale rijen, dan alle verticale, dan diagnoaal de ene kant, dan diagnonaal de andere kant.
        credits voor de logic van de code gaan naar MichaelEstes. Hij heeft deze logic gemaakt in c# en ik heb dit als template gebruikt voor de python code.
        '''
        XO = symbol
        win = False

        for i in range(self.height):
            for ix in range(self.width):
                if (self.board[i][ix] == XO and
                    self.board[i-1][ix-1] == XO and
                    self.board[i-2][ix-2] == XO and
                    self.board[i-3][ix-3] == XO ):
                    win = True

                if(self.board[i][ix] == XO and
                    self.board[i][ix-1] == XO and
                    self.board[i][ix-2] == XO and
                    self.board[i][ix-3] == XO ):
                    win = True
                        
                if( self.board[i][ix] == XO and
                    self.board[i-1][ix] == XO and
                    self.board[i-2][ix] == XO and
                    self.board[i-3][ix] == XO ):
                    win = True
                        
                if( self.board[i][ix] == XO and
                    self.board[i-1][ix+1] == XO and
                    self.board[i-2][ix+2] == XO and
                    self.board[i-3][ix+3] == XO ):
                    win = True
                            
                if ( self.board[i][ix] == XO and
                    self.board[i][ix+1] == XO and
                    self.board[i][ix+2] == XO and
                    self.board[i][ix+3] == XO ):
                    win = True
        return win

class player():
    pass


b = Board()
for i in range(3):
    b.placeDisk(2, 'r')
    print(b.board)
print(b.checkBoard('r'))
