### Classes and inheritance
'''
class Weichle(): ## SuperClass
    def __init__(self,price,gas,colour): ## attributes of the super class
        self.price = price
        self.gas = gas
        self.colour = colour
# self means instance within that class such as tim = Weicle(....) Timm is actually the self
    def fillUpTank(self):  ## methods of the superclass
        self.gas = 100

    def emptyTank(self):
        self.gas = 0

    def gasLeft(self):
        return self.gas

class Car(Weichle): #Children class
    def __init__(self,price,gas,colour,speed):###These 2 lines essantially inherits the attributes from the main superclass
        super().__init__(price,gas,colour)
        self.speed = speed

    def beep(self):
        print("Beep Beeep")

class Truck(Weichle):
    def __init__(self, price, gas, colour,tires):
        super().__init__(price, gas, colour)
        self.tires = tires
    def beep(self):
        print("Honk Honk!!")


bmw = Car(25.99,"diesel","blue",100)

bmw.beep()
'''
'''
class People():
    def __init__(self,name,phone_number,birthday):
        self.name=name
        self.phone_number = phone_number
        self.birthday=birthday
    def getAge(self,age):
        self.age=age

class Student(People):
    def __init__(self,name,phone_number,birthday,student_number,transkrip):
        super().__init__(name,phone_number,birthday)
        self.student_number=student_number
        self.transkrip=transkrip
    def avarageScore(self,overall):
        self.overall=overall
class Prof(People):
    def __init__(self, name, phone_number, birthday,wage):
        super().__init__(name, phone_number, birthday)
        self.wage=wage


erim = Student("Erim",5353754301,"27/03/1990",315514224,2.24)    
erim.getAge(27)
print(erim.age)
'''
### Overloading the default python modules
### You may check online for the default methods
### www.siafoo.net/article/57
'''
class Point():
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y
        self.coords = (self.x,self.y)

    def move(self,x,y):
        self.x += x
        self.y += y
    def __add__(self,p):
        return Point(self.x + p.x, self.y + p.y)
    def __sub__(self,p):
        return Point(self.x - p.x, self.y - p.y)
    def __mul__(self,p):
        return self.x * p.x + self.y * p.y
    def length(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)
    
    def __gt__(self,p):## Greater than
        return self.length() > p.length()
    def __ge__(self,p):##Greater or equal 
        return self.length() >= p.length()

    def __lt__(self,p):## Less Then
        return self.length() < p.length()
    def __le__(self,p):## Lesser or equal
        return self.length() <= p.length()
    def __eq__(self,p):## Equal to
        return self.x == p.x and self.y == p.y
    
    def __str__(self): ## convert the " gibberish into str"
        return "(" + str(self.x) + " , " + str(self.y) + ")"


p1 = Point(3,4)
p2 = Point(3,2)
p3 = Point(1,3)
p4 = Point(0,1)

print(p1==p2)
print(p1>p2)
print(p4<=p3)
'''
### Static methods and Class methods
class Dog():
    dogs = []

    def __init__(self,name):
        self.name=name
        self.dogs.append(self)

    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)

    @staticmethod
    def bar(n):
        #barks n times
        for _ in range(n):
            print("Bark!")


tim = Dog("Tim")
jim = Dog("Jim")

Dog.bar(5)