class Car:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
c1=Car(8,8,5)
print(c1.m1,c1.m2,c1.m3)
print(c1.avg())
