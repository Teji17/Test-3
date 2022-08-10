from abc import ABC, abstractmethod
class Polygon(ABC):
    @abstractmethod
    def perimeter(self):
        pass
    def area(self):
        pass

class Rectangle(Polygon):
    def perimeter(self, length, breadth):
        return 2 * (length + breadth)
    def area(self, length, breadth):
        return length * breadth

class Square(Polygon):
    def perimeter(self, length, sides):
        return sides * length
    def area(self, length):
        return length * length

class Pentagon(Polygon):
    def perimeter(self, length, sides):
        return sides * length
    def area(self, length, sides):
        return 1 / 2 * sides * length * length

length = int(input("enter length of polygon: "))
breadth = int(input("enter breadth of polygon: "))
side = int(input("enter sides of polygon: "))
R = Rectangle()
S = Square()
P = Pentagon()

if length!=breadth and side ==4:
    print("perimeter and area of rectangle are ")
    print(R.perimeter(length, breadth), R.area(length, breadth))
elif length==breadth and side==4:
    print("perimeter and area of square are ")
    print(S.perimeter(length, side), S.area(length))
elif length==breadth and side==5:
    print("perimeter and area of regular pentagon are ")
    print(P.perimeter(length, side), P.area(length, side))
else:
    print("polygon shape not available")
