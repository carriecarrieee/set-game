"""Implements a modified version of the real card game Set.
   Rules of the game Set: https://paper.dropbox.com/doc/lYHYZDoLQtlINtyyEYSVi"""


from random import shuffle


class SetCard(object):
    """Models a Set card, and each card has a shape, shading, and count."""

    def __init__(self, shape, shading, count):
        self.shape = shape
        self.shading = shading
        self.count = count


    def __repr__(self):
        print [self.shape, self.shading, self.count]

        
class SetGame(SetCard):
    """Generates deck of 27 Set cards that is stored within the class instance
       on initialization.
    """
    
    def __init__(self):
        super(SetCard, self).__init__()
        self.table = [] # List that tracks cards currently on table

        shapes = ["oval", "squiggle", "diamond"]
        shadings = ["solid", "striped", "open"]
        counts = [1, 2, 3]
        
        deck = [Card(shape, shading, count) for shape in shapes \
                                            for shading in shadings \
                                            for count in counts]

    def deal(self, num_cards):
        shuffle(self.deck)

        for i in range(num_cards):
            if self.deck.is_empty():
                break
            self.table.append(deck.pop())

        return self.table
            

    def is_set(self, card1, card2, card3):
        pass


    def find_set():
        pass


 