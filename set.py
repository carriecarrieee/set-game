"""Implements a modified version of the real card game Set.
   Rules of the game Set: https://paper.dropbox.com/doc/lYHYZDoLQtlINtyyEYSVi"""


from random import shuffle


class SetCard:
    """Models a Set card, and each card has a shape, shading, and count."""

    # Class attributes
    shapes = ["oval", "squiggle", "diamond"]
    shadings = ["solid", "striped", "open"]
    counts = [1, 2, 3]


    def __init__(self, shape="oval", shading="solid", count=1): # default card
        
        self.shape = shape
        self.shading = shading
        self.count = count


    def __repr__(self):
        """Prints representation of a SetCard"""

        return "{}, {}, {}".format(self.shape, self.shading, self.count)

        
class SetGame:
    """Generates deck of 27 Set cards that is stored within the class instance
       on initialization.
    """
    
    def __init__(self):
        
        self.deck = [SetCard(shape, shading, count) \
            for shape in SetCard.shapes \
            for shading in SetCard.shadings \
            for count in SetCard.counts]

        self.table = [] # List that tracks cards currently on table


    def __repr__(self):
        """Prints string representation of deck."""

        deck_lst = []

        for card in self.deck:
            deck_lst.append(str(card))

        return "\n".join(deck_lst)


    def deal(self, num_cards):
        """In a game of Set, cards are dealt onto the table at a given time. 
           The instance variable "table" tracks the cards that are currently on
           the table. This function deals num_cards random cards onto the table 
           from the deck.
        """

        self.num_cards = num_cards # Number of cards to be dealt

        shuffle(self.deck) # Shuffle cards before dealing

        for i in range(num_cards):
            if not self.deck: # In case the deck is empty
                raise Exception("Deck is empty! Please create new deck.")

            # Pops num_cards off of the deck and adds it to table
            self.table.append(self.deck.pop())

        return self.table # list of SetCard instances


    def is_set(self, card1, card2, card3):
        """Accepts three cards and returns a boolean indicating whether the 
           three cards make up a valid set. A set is valid if all three
           conditions hold:
            1. Shape: all the same shape OR all different shapes
            2. Shading: all the same shading OR all different shading
            3. Count: all the same count OR all different count
        """

        self.card1 = card1
        self.card2 = card2
        self.card3 = card3

        # True if game conditions for a valid set hold; False otherwise
        return ((card1.shape == card2.shape == card3.shape) or \
                (card1.shape != card2.shape and \
                 card2.shape != card3.shape and \
                 card1.shape != card3.shape)) and \
               ((card1.shading == card2.shading == card3.shading) or \
                (card1.shading != card2.shading and \
                 card2.shading != card3.shading and \
                 card1.shading != card3.shading)) and \
               ((card1.count == card2.count == card3.count) or \
                (card1.count != card2.count and \
                 card2.count != card3.count and \
                 card1.count != card3.count))


    def find_set(self):
        """Finds one possible set among the table cards and prints it out. The 
           function returns a boolean indicating whether or not a set was found.
        """

        for card1 in self.table:
            for card2 in self.table:
                for card3 in self.table:
                    if card1 != card2 != card3:
                        if self.is_set(card1, card2, card3):
                            print card1, card2, card3
                            return True

        print "Sorry, no set found."
        return False



if __name__ == "__main__":

    print "\nNew card with default values:\n"
    myCard = SetCard()
    print myCard
    print "\n****************************************\n"

    print "New deck from an instantiation of SetGame:\n"
    myGame = SetGame()
    print myGame
    print "\n****************************************\n"

    print "List of cards that were dealt from the deck onto the table:\n"
    myGame.deal(4)
    myGame.deal(5)
    for card in myGame.table:
        print card
    print "\n****************************************\n"

    print "Let's see if there's a set currently on the table:\n"
    print myGame.find_set()
    print "\n****************************************\n"