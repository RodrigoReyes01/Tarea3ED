from typing import NamedTuple


class User(NamedTuple):
    name: str


class MyStruct(NamedTuple):
    puntoX: float
    puntoY: float
    X: str
    Y: str
    Cuadrante: int

x= int(input("ingrese el punto X: "))
y= int(input("ingrese el punto Y: "))
if (x > 0):
    a = "positive"
elif (x < 0):
    a = "negative"
else:
    a = ("no es ni negativo ni positivo")

if (y > 0):
    b = "positive"
elif (y < 0):
    b = "negative"
else:
    b = ("no es ni negativo ni positivo")

if (a == "positive" and b== "positive"):
    c = 1
elif(a == "negative" and b== "positive"):
    c = 2
elif(a == "negative" and b== "negative"):
    c = 3
elif(a == "positive" and b== "negative"):
    c = 4


my_item = MyStruct(x, y, a, b, c)

print(my_item) # MyStruct(foo='foo', bar=0, baz=['baz'], qux=User(name='peter'))