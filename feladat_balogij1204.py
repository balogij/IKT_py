class Ember:
    def __init__(self, nev='', kor=0):
        self.nev = nev
        self.kor = kor
    def __str__(self):
        return f'{self.nev} ({self.kor} éves)'
    def Maxkor(self, masik):
        if self.kor > masik.kor:
            return self
        else:
            return masik

class Auto:
    def __init__(self, marka='', tipus='', evjarat=0):
        self.marka = marka
        self.tipus = tipus
        self.evjarat = evjarat
    def kiir(self):
        return f'Márka: {self.marka}, Típus: {self.tipus}, Évjárat: {self.evjarat}'
class BankSzamla:
    def __init__(self, nev='', szamlaszam='', egyenleg=0.0):
        self.nev = nev
        self.szamlaszam = szamlaszam
        self.egyenleg = egyenleg
    def befizetes(self, osszeg):
        self.egyenleg += osszeg
    def kivesz(self, osszeg):
        if osszeg > self.egyenleg:
            print('Nincs elég egyenleg!')
        else:
            self.egyenleg -= osszeg
    def kiir(self): 
        return f'Név: {self.nev}, Számlaszám: {self.szamlaszam}, Egyenleg: {self.egyenleg} Ft'

class Student:
    def __init__(self, nev='', eletkor=0, atlag=0.0):
        self.nev = nev
        self.eletkor = eletkor
        self.atlag = atlag
    def kiir(self):
        return f'Név: {self.nev}, Életkor: {self.eletkor}, Átlag: {self.atlag}'

#feladatok listája
feladatok = ['1. feladat – Faktoriális számítása ciklussal. Kérj be egy számot, és számold ki a faktoriálisát iterációval.','2. feladat – Kérj be egy N számot, és számold ki az 1-től N-ig terjedő számok szorzatát (faktoriális ELLENTÉTE: itt nem csak N!, hanem általánosan 1·2·3…·N).','3. feladat – Prímszám ellenőrzése. Döntsd el egy számról, hogy prímszám-e (szelekció + iteráció).','4. feladat – Számjegyek összege. Kérj be egy számot, majd számold ki a számjegyeinek összegét.','5. feladat – Lista elemeinek négyzetre emelése. Adott egy lista, készíts új listát, amely minden elem négyzetét tartalmazza.','6. feladat – Szótár gyakorlás. Kérj be 5 nevet és életkort, majd tárold őket egy dict-ben. Ezután írd ki a legidősebb személy nevét.','7. feladat – OOP: Egyszerű Osztály. Hozz létre egy Auto osztályt, amely attribútumai: márka, típus, évjárat. Az osztály tartalmazzon metódust, ami kiírja a teljes adatot szép formában.','9. feladat – OOP + lista: Tanulók kezelése. Student osztály: név, életkor, átlag.Kérj be 3 tanulót, tedd őket listába, majd írd ki annak a nevét, akinek a legjobb az átlaga.','10. feladat – OOP: Öröklődés. Készíts egy Allat alaposztályt (név, életkor).Készíts két leszármazottat: Kutya (plusz: fajta) Macska (plusz: szín) Mindkettőnek legyen hang() metódusa, ami kiírja a saját hangját. Példányosítsd őket és hívd meg a metódust.']

countFeladat = len(feladatok)

#main
fut = True
while (fut):
    nemszam = True
    while(nemszam):
        bevitel = input(f'Melyik feladatot választod (1-{countFeladat} vagy "K" kilépés) : ')
        try:
            sorszam = int(bevitel)
            nemszam = False
        except ValueError:
            if(bevitel == 'k'):
                nemszam = False
                fut = False
                print('Viszlát!')
            else:
                print('Ez nem szám!')
    if fut:
        sorszam = int(bevitel)
        print(sorszam)
        match(sorszam):
            #első feladat
            case 1:
                print(feladatok[sorszam-1])
                print('Megoldas:')
                notnumber = True
                while(notnumber):
                    try:
                        elso = int(input('Adj meg egy pozitív egész számot: '))
                        if elso < 0:
                            print('A szám nem lehet negatív!')
                        else:
                            notnumber = False
                    except ValueError:
                        print('Ez nem egész szám!')
                    f = elso
                for i in range(1,elso):
                    f = f * i
                print(f'A {elso} faktoriálisa: {f}')
            #második feladat
            case 2:
                print(feladatok[sorszam-1])
                print('Megoldas:')
                notnumber = True
                while(notnumber):
                    try:
                        elso = int(input('Adj meg egy pozitív egész számot: '))
                        notnumber = False
                    except ValueError:
                        print('Ez nem egész szám!')
                    f = elso
                if elso>=0:
                    for i in range(1,elso):
                        f = f * i
                else:
                    for i in range(elso,1):
                        f = f * i
                print(f'A 1-től {elso}-ig terjedő számok szorzata: {f}')
            #harmadik feladat
            case 3:
                print(feladatok[sorszam-1])
                print('Megoldas:')
                notnumber = True
                while(notnumber):
                    try:
                        elso = int(input('Adj meg egy pozitív egész számot: '))
                        notnumber = False
                    except ValueError:
                        print('Ez nem egész szám!')
                if elso<2:
                    print(f'A {elso} nem prímszám.')
                else:
                    szam = int(3)
                    oszto = int(2)

                    prim = False
                    for i in range(2,int(elso**0.5)+1):
                        if elso % i == 0:
                            prim = True
                            break 
                    if prim==True:
                        print(f'A {elso} nem prímszám.')
                    else:
                        print(f'A {elso} prímszám.')
            #negyedik feladat
            case 4:
                print(feladatok[sorszam-1])
                print('Megoldas:')
                notnumber = True
                while(notnumber):
                    try:
                        elso = int(input('Adj meg egy pozitív egész számot: '))
                        notnumber = False
                    except ValueError:
                        print('Ez nem egész szám!')
                osszeg = 0
                szamok = [int(i) for i in str(elso)]
                for i in szamok:
                    osszeg += i
                print(f'A {elso} számjegyeinek összege: {osszeg}')
            #ötödik feladat
            case 5:
                print(feladatok[sorszam-1])
                print('Megoldas:')
                lista = [2,3,5,8,11,34,82]
                ujlista = []
                for i in lista:
                    ujlista.append(i**2)
                for i in range(len(ujlista)):
                    print(f'A(z) {i+1}. elem négyzete: {ujlista[i]}')
            #hatodik feladat
            case 6:
                print(feladatok[sorszam-1])
                print('Megoldas:')
                emberek = {}

                for i in range(5):
                    nev = str(input('Adj meg egy nevet: '))
                    notnumber = True
                    while(notnumber):
                        try:
                            kor = int(input('Add meg a korát: '))
                            if kor < 0:
                                print('A kor nem lehet negatív!')
                            else:
                                notnumber = False
                        except ValueError:
                            print('Ez nem egész szám!')                        
                    emberek[nev] = kor
                legidosebb = max(emberek, key=emberek.get)
                print(f'A legidősebb személy: {legidosebb}, kora: {emberek[legidosebb]} éves.')
            #hetedik feladat
            case 7:
                print(feladatok[sorszam-1])
                print('Megoldas:')
                auto = Auto()
                auto.marka = str(input('Add meg a márkát: '))
                auto.tipus = str(input('Add meg a típust: '))
                notnumber = True
                while(notnumber):
                    try:
                        auto.evjarat = int(input('Adj meg egy pozitív egész számot: '))
                        notnumber = False
                    except ValueError:
                        print('Ez nem egész szám!')   
                print('Az autó adatai:')
                print(auto.kiir())                       
            #nyolcadik feladat
            case 8:
                print(feladatok[sorszam-1])
                print('Megoldas:')
                szamla = BankSzamla()
                szamlak = []
                for _ in range(1):
                    szamla.nev = str(input('Add meg a számla tulajdonosának nevét: '))
                    szamla.szamlaszam = str(input('Add meg a számlaszámot: '))

                    notnumber = True
                    while(notnumber):
                        try:
                            szamla.egyenleg = float(input('Add meg az egyenleget: '))
                            notnumber = False
                        except ValueError:
                            print('Ez nem szám!')  
                    print('A számla adatai:')
                    print(szamla.kiir())    
                    szamlak.append(szamla)
                notnumber = True
                while(notnumber):
                    try:
                        szamlaszam = str(input('Add meg a számlaszámot ellenőrzésre: '))
                        if szamlaszam != szamla.szamlaszam:
                            print('Hibás számlaszám!')
                        else:
                            notnumber = False
                        osszeg = float(input('Adj meg egy befizetési összeget: '))
                        szamla.befizetes(osszeg)
                        print(f'{szamla.nev} új egyenlege: {szamla.egyenleg} Ft')
                        notnumber = False
                    except ValueError:
                        print('Ez nem szám!')   
                notnumber = True
                while(notnumber):   
                    try:
                        szamlaszam = str(input('Add meg a számlaszámot ellenőrzésre: '))
                        if szamlaszam != szamla.szamlaszam:
                            print('Hibás számlaszám!')
                        else:
                            notnumber = False
                        osszeg = float(input('Adj meg egy kiveendő összeget: '))
                        szamla.kivesz(osszeg)
                        print(f'{szamla.nev} új egyenlege: {szamla.egyenleg} Ft')
                        notnumber = False
                    except ValueError:
                        print('Ez nem szám!')                                      
