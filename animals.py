#create parent class
class Things:
    pass

class Alive(Things):
    def breathe(self):
        print('breathing')

class Animals(Alive):
    def eat(self):
        print('eating')
    def poop(self):
        print('pooping💩')
    def move(self):
        print('moving😎')

class Mammals(Animals):
    def feed_young_with_milk(self):
        print('feeding young with milk')

class Giraffes(Mammals):
    def __init__(self, spots):
        self.giraffe_spots = spots