from typing import NamedTuple
import function3 as fun


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

myx_values = fun.valx(x)
my_values = fun.valy(y)
#print(myx_values,my_values)
quadrant = fun.findCua (x,y)
#print(quadrant)


my_item = MyStruct(x, y, fun.valx(x), fun.valy(y), fun.findCua(x,y))
print(my_item)
