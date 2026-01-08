keresztnev = input('Adja meg a keresztnevét:')
eletkor_num = int(input('Adja meg az életkorát'))

if(eletkor_num<1):
    print(f'A kora alapján {keresztnev} csecsemő!')
elif(eletkor_num<6):
    print(f'A kora alapján {keresztnev} kisgyerek!')
elif(eletkor_num<12):
    print(f'A kora alapján {keresztnev} gyerek!')
elif(eletkor_num<16):
    print(f'A kora alapján {keresztnev} serdülő!')
elif(eletkor_num<25):
    print(f'A kora alapján {keresztnev} ifjú!')
elif(eletkor_num<65):
    print(f'A kora alapján {keresztnev} felnőtt!')
else:
    print(f'A kora alapján {keresztnev} nyugdíjas!')
