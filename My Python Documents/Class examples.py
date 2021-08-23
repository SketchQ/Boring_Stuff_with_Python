

from datetime import date
'''

class Student():
    def __init__(self,name,phone,birthday):
        self.name = name
        self.phone = phone
        self.birthday = birthday
    
    


Erim=Student("Erim", 232450592, 27_03_90)

print("Name of this student is : " + Erim.name.title())
print("Phone number of this student is : " + str(Erim.phone))
print("Birthday of this student is : " + str(Erim.birthday))



class Rectangle():
    def __init__(self, length, breadth, unit_cost=0):
        self.lenght = length
        self.breadth = breadth
        self.unit_cost = unit_cost
    def get_area(self):
        return self.lenght * self.breadth
    def calculate_cost(self):
        area = self.get_area()
        return area * self.unit_cost

v = Rectangle(150, 200, 5000)
print(v.get_area())
print(v.calculate_cost())
             
def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
           
'''


class Ucus():
   
    def __init__(self,kod,kalkis,varis,sure,kapasite,yolcu):
        self.kod = kod
        self.kalkis = kalkis
        self.varis = varis
        self.sure = sure
        self.kapasite = kapasite
        self.yolcu = yolcu
        self.ucak_tipi = 777

    def anons_kalkis(self):
        print(ucus1.kalkis + " 'dan " + ucus1.varis + " 'ya seyahat edecek olan " + ucus1.kod + " 'no'lu seyahat yolcuları uçağınız kalkışa hazırdır.")
    def ucak_tipi_degisim(self, update):
        self.ucak_tipi = update
    

ucus1 = Ucus("tk101","IST","ANK",60,175,125)

print(ucus1.anons_kalkis())
"""ucus1.ucak_tipi_degisim(737)"""
print(ucus1.ucak_tipi)