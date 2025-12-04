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
        
#feladatok listája
feladatok = ['1. feladat – Faktoriális számítása ciklussal. Kérj be egy számot, és számold ki a faktoriálisát iterációval.','2. feladat – Kérj be egy N számot, és számold ki az 1-től N-ig terjedő számok szorzatát (faktoriális ELLENTÉTE: itt nem csak N!, hanem általánosan 1·2·3…·N).','3. feladat – Prímszám ellenőrzése. Döntsd el egy számról, hogy prímszám-e (szelekció + iteráció).','4. feladat – Számjegyek összege. Kérj be egy számot, majd számold ki a számjegyeinek összegét.','5. feladat – Lista elemeinek négyzetre emelése. Adott egy lista, készíts új listát, amely minden elem négyzetét tartalmazza.','6. feladat – Szótár gyakorlás. Kérj be 5 nevet és életkort, majd tárold őket egy dict-ben. Ezután írd ki a legidősebb személy nevét.']

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
                emberek = []
                curent = Ember()

                for i in range(5):
                    curent.nev = str(input('Adj meg egy nevet: '))
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
                    curent.kor = kor
                    emberek.append(curent)
                    curent = Ember()
                legidosebb = emberek[0]
                for i in emberek:
                    legidosebb = legidosebb.Maxkor(i)
                print(f'A legidősebb személy: {legidosebb.nev}, kora: {legidosebb.kor} éves.')

            #hetedik feladat
            case 7:
                print(feladatok[sorszam-1])
                print('Megoldas:')
                notnumber = True
                while(notnumber):
                    try:
                        elso = int(input('Adj meg egy pozitív egész számot: '))
                        notnumber = False
                    except ValueError:
                        print('Ez nem egész szám!')                        
