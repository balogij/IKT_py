def ertekeles(pont,bonusz):
    if(pont+2*bonusz>100 or bonusz>10):
        return "MEGFELELT"
    else:
        return "NEM FELELT MEG"
    
fut = True
while(fut):
    nev = input('Adja meg a nevet: ')
    if(nev==''):
        fut = False
    else:
        pont = int(input('Adja meg az elért pontot: '))
        bonusz = int(input('Adja meg az elért bonusz pontot: '))
        print(f'{nev} tesztjének minősítése: {ertekeles(pont,bonusz)}')