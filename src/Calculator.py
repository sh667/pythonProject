from math import *


class Calculator:
    result=0
    def __init__(self):
        pass
    def minus(self, x, y):
        x = float(x)
        y = float(y)
        return   float(y)-float(x)
    def plus(self, x, y):
          x=float(x)
          y=float(y)
          return float(x) + float(y)