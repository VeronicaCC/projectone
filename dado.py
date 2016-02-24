import math
class Dado (object):
    def __init__(self, x=0):
        self.x=x

    def __eq__ (self, otro):
        return self.x== otro.x

    def __str__(self):
        return [self.x,"Caras"]

