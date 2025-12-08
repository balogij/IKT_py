class test:
    def __init__(self,szam=0,szoveg=""):
        self.szam = input('Add meg a számot: ') 
        self.szoveg= input('Add meg a szöveget: ')
    def kiir(self):
        print(f'A szám: {self.szam}, a szöveg: {self.szoveg}')
    def osszead(self,masik):
        return int(self.szam) + int(masik.szam)
    def nagyobb(self,masik):
        if int(self.szam) > int(masik.szam):
            return self.szoveg
        else:
            return masik.szoveg
    def szorzas(self,masik):
        return int(self.szam) * int(masik.szam)
    def hatvany(self,masik):
        return int(self.szam) ** int(masik.szam)
    def osztas(self,masik):
        if int(masik.szam) != 0:
            return int(self.szam) / int(masik.szam)
        else:
            return "Nullával való osztás nem lehetséges!"

#main
obj1 = test()
obj2 = test()
obj1.kiir()
obj2.kiir()
print(f'Összeadás {obj1.szam} + {obj2.szam}: {obj1.osszead(obj2)}')
print(f'Nagyobb számot megadó név: {obj1.nagyobb(obj2)}')
print(f'Szorzás {obj1.szam} * {obj2.szam}: {obj1.szorzas(obj2)}')
print(f'Hatványozás {obj1.szam} ** {obj2.szam}: {obj1.hatvany(obj2)}')
print(f'Osztás {obj1.szam} / {obj2.szam}: {obj1.osztas(obj2)}')