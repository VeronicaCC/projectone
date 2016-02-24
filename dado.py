import math
class Dado (object):
    def __init__(self, x=0):
        self.x=x

    def __eq__ (self, otro):
        return self.x== otro.x

    def __str__(self):
        return [self.x,"Caras"]

    def tira (self):
        self.y = random.randrange(1, (self.x)+1, 1)

    def fija_valor (self,c):
       if c<=self.x: self.y = c
       if c>self.x: print ("Error: El valor fijado es mayor que el número de caras")

        
    def obtener_valor (self):
        print (self.y)
