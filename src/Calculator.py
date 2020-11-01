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
    def multiple(self, x, y):
        x = float(x)
        y = float(y)
        return float(x) * float(y)
    def divide(self, x, y):
        x = float(x)
        y = float(y)
        return float(y) / float(x)
    def square(self, x):
        x = float(x)
        return (float(x**2))
    def squareroot(self, x):
        x = float(x)
        return float(sqrt(x))
