class Vehicle(object):
    def __init__(self, maker, color , year):
        self.maker = maker
        self.color = color
        self.year = year

    def getveicle(self):  # getter
        return self.maker, self.color, self.year

    def setvicle(self):  # setter
        self.maker = str
        self.color = str
        self.year = int

    def show(self):  # print
        print("maker:", self.maker)
        print('color:', self.color)
        print("year:", self.year)


a = Vehicle('hyundai', 'red', 20201201)



class truck(Vehicle):
    def __init__(self, maker , color , year, horse_power):
        super(truck, self).__init__(maker,color,year)
        self.horse_power = horse_power

    def gettruck(self): #getter
        return self.horse_power

    def settruck(self): #setter
        self.horse_power = int

    def show_mathod(self):
        super(truck,self).show()
        print('horse_power:', self.horse_power)


b = truck('hyundai', 'blue', 20201201, 1000)

b.show_mathod()
