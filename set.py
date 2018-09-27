"""Implements a modified version of the real card game Set.
   Rules of the game Set: https://paper.dropbox.com/doc/lYHYZDoLQtlINtyyEYSVi"""


from random import shuffle


class SetCard:
    """Models a Set card, and each card has a shape, shading, and count."""

    def __init__(self, shape, shading, count):
        self.shape = shape
        self.shading = shading
        self.count = count


    def __repr__(self):
        """Prints representation of a SetCard:

        >>> newCard = SetCard('oval', 'striped', 3)
        >>> newCard.__repr__()
        ['oval', 'striped', 3]

        """

        print [self.shape, self.shading, self.count]

        
class SetGame(SetCard):
    """Generates deck of 27 Set cards that is stored within the class instance
       on initialization.
    """
    
    def __init__(self):

        shapes = ["oval", "squiggle", "diamond"]
        shadings = ["solid", "striped", "open"]
        counts = [1, 2, 3]
        
        self.deck = [SetCard(shape, shading, count) for shape in shapes \
                                                    for shading in shadings \
                                                    for count in counts]


    def deal(self, num_cards):
        """In a game of Set, cards are dealt onto the table at a given time. 
           The instance variable "table" tracks the cards that are currently on
           the table. This function deals num_cards random cards onto the table 
           from the deck.

           myGame = SetGame()
           myGame.deal(4)
        """

        self.num_cards = num_cards # Number of cards to be dealt
        self.table = [] # List that tracks cards currently on table

        shuffle(self.deck) # Shuffle cards before dealing

        for i in range(num_cards):
            if not self.deck: # In case the deck is empty
                print "Deck is empty!"
                break

            # Pops num_cards off of the deck and adds it to the table list
            self.table.append(self.deck.pop())

        return self.table
# myGame = SetGame()
# print myGame.deal(4)        

# How do I print self.table without overriding the __repr__ method in superclass?

    def is_set(self, card1, card2, card3):
        """Rules of the game Set: 
           https://paper.dropbox.com/doc/lYHYZDoLQtlINtyyEYSVi
    
           Accepts three cards and returns a boolean indicating whether the 
           three cards make up a valid set. A set is valid if all three
           conditions hold:
            1. Shape: all the same shape OR all different shapes
            2. Shading: all the same shading OR all different shading
            3. Count: all the same count OR all different count

            >>> myGame = SetGame()
            >>> myGame.is_set(["oval", "solid", 1], ["oval", "solid", 2], ["oval", "solid", 3])
            True

            >>> myGame.is_set(["oval", "solid", 1], ["oval", "striped", 2], ["oval", "solid", 3])
            False
        """

        self.card1 = card1
        self.card2 = card2
        self.card3 = card3

        # Using temp variable names for easier reference
        shape1 = card1[0]
        shape2 = card2[0]
        shape3 = card3[0]

        shading1 = card1[1]
        shading2 = card2[1]
        shading3 = card3[1]

        count1 = card1[2]
        count2 = card2[2]
        count3 = card3[2]

        return ((shape1 == shape2 == shape3) or \
                (shape1 != shape2 and \
                 shape2 != shape3 and \
                 shape1 != shape3)) and \
               ((shading1 == shading2 == shading3) or \
                (shading1 != shading2 and \
                 shading2 != shading3 and \
                 shading1 != shading3)) and \
               ((count1 == count2 == count3) or \
                (count1 != count2 and \
                 count2 != count3 and \
                 count1 != count3))

    def find_set():
        pass



if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if result.failed == 0:
        print "ALL TESTS PASSED"