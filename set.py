"""Implements a modified version of the real card game Set.
   Rules of the game Set: https://paper.dropbox.com/doc/lYHYZDoLQtlINtyyEYSVi"""

class SetCard(object):
    """Models a Set card, and each card has a shape, shading, and count.
       Possible values for each attribute are:

        shapes = ["oval", "squiggle", "diamond"]
        shadings = ["solid", "striped", "open"]
        counts = [1, 2, 3]
    """

    def __init__(self, shape, shading, count):
        self.shape = shape
        self.shading = shading
        self.count = count

        shapes = ["oval", "squiggle", "diamond"]
        shadings = ["solid", "striped", "open"]
        counts = [1, 2, 3]

    def __repr__(self):
        print self.shape, self.shading, self.count

        
class SetGame(SetCard):
    """Generates deck of 27 Set cards that is stored within the class instance
       on initialization.
    """
        def __init__(self):
            super(SetCard, self).__init__()

            deck = [Card(shape, shading, count) for shape in shapes \
                                                for shading in shadings \
                                                for count in counts]

        

