"""Implements a modified version of the real card game Set.
   Rules of the game Set: https://paper.dropbox.com/doc/lYHYZDoLQtlINtyyEYSVi"""


from random import shuffle


class SetCard:
    """ Models a Set card, and each card has a shape, shading, and count."""

    # Class attributes
    shapes = ["oval", "squiggle", "diamond"]
    shadings = ["solid", "striped", "open"]
    counts = [1, 2, 3]


    def __init__(self, shape, shading, count):
        
        self.shape = shape
        self.shading = shading
        self.count = count


    def __repr__(self):
        """ Prints representation of a SetCard.

            Test:

            >>> myCard = SetCard('oval', 'striped', 3)
            >>> print myCard
            oval, striped, 3

            """

        return "{}, {}, {}".format(self.shape, self.shading, self.count)

        
class SetGame:
    """ Generates deck of 27 Set cards that is stored within the class instance
        on initialization. (HAS-A relationship)
    """
    
    def __init__(self):
        
        self.deck = [SetCard(shape, shading, count) \
            for shape in SetCard.shapes \
            for shading in SetCard.shadings \
            for count in SetCard.counts]

        self.table = [] # List that tracks cards currently on table


    def __repr__(self):
        """ Prints string representation of deck.

            Test:

            >>> myGame = SetGame()
            >>> print myGame.deck
            [oval, solid, 1, oval, solid, 2, oval, solid, 3, oval, striped, 1, oval, striped, 2, oval, striped, 3, oval, open, 1, oval, open, 2, oval, open, 3, squiggle, solid, 1, squiggle, solid, 2, squiggle, solid, 3, squiggle, striped, 1, squiggle, striped, 2, squiggle, striped, 3, squiggle, open, 1, squiggle, open, 2, squiggle, open, 3, diamond, solid, 1, diamond, solid, 2, diamond, solid, 3, diamond, striped, 1, diamond, striped, 2, diamond, striped, 3, diamond, open, 1, diamond, open, 2, diamond, open, 3]


        """

        deck_lst = []

        for card in self.deck:
            deck_lst.append(str(card))

        return "\n".join(deck_lst)


    def deal(self, num_cards):
        """ In a game of Set, cards are dealt onto the table at a given time. 
            The instance variable "table" tracks the cards that are currently on
            the table. This function deals num_cards random cards onto the table 
            from the deck.

            Test:
            
            >>> myGame = SetGame()
            >>> len(myGame.deal(4))
            4

            >>> len(myGame.deal(5))
            9

            >>> len(myGame.table)
            9

        """

        shuffle(self.deck) # Shuffle cards before dealing

        for i in range(num_cards):
            if not self.deck: # In case the deck is empty
                raise Exception("Deck is empty! Please create new deck.")

            # Pops num_cards off of the deck and adds it to table
            self.table.append(self.deck.pop())

        return self.table # list of SetCard instances


    def is_set(self, card1, card2, card3):
        """ Accepts three cards and returns a boolean indicating whether the 
            three cards make up a valid set. A set is valid if all three
            conditions hold:
            1. Shape: all the same shape OR all different shapes
            2. Shading: all the same shading OR all different shading
            3. Count: all the same count OR all different count

            True if game conditions for a valid set hold; False otherwise.

            Test:

            >>> card1 = SetCard('oval', 'striped', 1)
            >>> card2 = SetCard('diamond', 'striped', 2)
            >>> card3 = SetCard('squiggle', 'striped', 3)
            >>> myGame = SetGame()
            >>> myGame.is_shape_valid(card1, card2, card2)
            False
            >>> myGame.is_shading_valid(card1, card2, card3)
            True
            >>> myGame.is_count_valid(card1, card1, card2)
            False
            >>> myGame.is_set(card1, card2, card3)
            True
            >>> myGame.is_set(card1, card2, card2)
            False
        """

        return self.is_shape_valid(card1, card2, card3) and \
               self.is_shading_valid(card1, card2, card3) and \
               self.is_count_valid(card1, card2, card3)


    def is_shape_valid(self, card1, card2, card3):
        """ Returns True if the shape attribute is valid, False otherwise."""

        return (card1.shape == card2.shape == card3.shape) or \
                (card1.shape != card2.shape and \
                 card2.shape != card3.shape and \
                 card1.shape != card3.shape)


    def is_shading_valid(self, card1, card2, card3):
        """ Returns True if the shading attribute is valid, False otherwise."""

        return (card1.shading == card2.shading == card3.shading) or \
                (card1.shading != card2.shading and \
                 card2.shading != card3.shading and \
                 card1.shading != card3.shading)


    def is_count_valid(self, card1, card2, card3):
        """ Returns True if the count attribute is valid, False otherwise."""

        return (card1.count == card2.count == card3.count) or \
                (card1.count != card2.count and \
                 card2.count != card3.count and \
                 card1.count != card3.count)


    def find_set(self):
        """ Finds one possible set among the table cards and prints it out.
            The function returns a boolean indicating whether or not a set was found.
        """

        if len(self.table) >= 3:
            for i in range(len(self.table)):
                for j in range(len(self.table[1:])):                
                    for k in range(len(self.table[2:])):
                        if self.table[i] != self.table[j] and \
                           self.table[j] != self.table[k] and \
                           self.table[i] != self.table[k] and \
                           self.is_set(self.table[i], self.table[j], self.table[k]):
                                print self.table[i], self.table[j], self.table[k]
                                return True

        print "Sorry, no set found."
        return False

# loop through indices i.e. for i in range(0, len(self.table))

if __name__ == "__main__":

    import doctest

    myGame = SetGame()
    myGame.deal(4)
    myGame.deal(5)
    for card in myGame.table:
        print card

    print "\nSet currently on the table?\n"
    print myGame.find_set()

    result = doctest.testmod()
    if result.failed == 0:
        print "\nALL TESTS PASSED"
