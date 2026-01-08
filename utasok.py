class Utas:
    def __init__(self,kedv = 0,km = 0):
        self.kedv = kedv
        self.km = km
        self.jegyar = km*50.0*(1.0-(kedv/100))
    
    def kmar(self):
        return self.jegyar/self.km
    
    def jegytipus(self):
        if(self.kedv == 0):
            return 'Teljes'
        elif(self.kedv==50):
            return 'Diák'
        elif(self.kedv==90):
            return 'Nyugdíjas'
        else:
            return 'Egyébb'

utasok = []
for i in range(8):
    kedv = int(input('Adja meg hány százalékos kedvezményt szeretne: '))
    km = int(input('Adja meg hány kilométert fog utazni:'))
    if(km==0):
        break
    else:
        utas_input = Utas(kedv,km)
        utasok.append(utas_input)

for cur_utas in utasok:
    print(f'{cur_utas.jegytipus()}({cur_utas.kedv}%), 1 kilométer ára: {cur_utas.kmar()} Forint')