class Rectangle:
    def __init__(self, r):
        self.le = int(input("ENTER THE LENGTH : "))
        self.br = int(input("ENTER THE BREADTH : "))
        a = self.perimeter()
        b = self.area()
        print("PERIMETER OF RECTANGLE : ", a)
        print("AREA OF RECTANGLE : ", b)

    def perimeter(self):
        return 2 * (self.le + self.br)

    def area(self):
        return self.le * self.br


class Circle:
    def __init__(self):
        self.ra = int(input("ENTER THE RADIUS : "))
        a = self.circumference()
        b = self.area()
        print("CIRCUMFERENCE OF CIRCLE : ", a)
        print("AREA OF CIRCLE : ", b)

    def circumference(self):
        return 2 * 3.14 * self.ra

    def area(self):
        return 3.14 * self.ra * self.ra


class Triangle:
    def __init__(self):
        self.a = int(input("ENTER THE LENGTH : "))
        self.b = int(input("ENTER THE BREADTH : "))
        self.c = int(input("ENTER THE HEIGHT : "))
        d = self.perimeter()
        e = self.area()
        print("PERIMETER OF TRIANGLE : ", d)
        print("AREA OF TRIANGLE : ", e)

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        return (self.b * self.c) / 2


r = Rectangle(2)
c = Circle()
t = Triangle()
