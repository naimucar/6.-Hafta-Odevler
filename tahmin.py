import random
kucuk=[0]
buyuk=[100]
while True:#baslatma inputu
    basla=input("""
___________________________________________________________

                    OYUN BASLASIN
                AKLINDAN BIR SAYI TUT VE....
    BASLA(ENTER)                       (Q)CIKIS
___________________________________________________________"""'\n')

    if basla=='q' or basla=='Q':
        print ( 'cikiliyor... ' )
        quit()
    elif basla!='':
        print('>>>>>>>>>>>>>>>>>>>>>>Hata lutfen baslamak icin ENTER tusuna basiniz>>>>>>>>>>>>>>>>>>>>>>>>>\n')
        continue
    elif  basla=='':
        print('\nOYUN BASLIYOR..............................................')
        break
    
while True:#OYUN DONGUSU

    if kucuk[-1]>=buyuk[0]: #  kullanicinin akli karismasin bilgisayari kandiramasin diye
        print('\nBENI KANDIRMAYAMI CALISIYORSUN {} SAYISINDAN BASKASI OLAMAZ'.format(tahmin))
        print('OYUN YENIDEN BASLIYOR........................................' , '\n' * 4)
        kucuk = [0]
        buyuk = [100]
        continue
    # BU DONGU ONEMLI
    #RANDOM ILE ; KUCUK LISTESININ EN BUYUGU ILE
    #BUYUK LISTESININ EN KUCUK ELEMANI ARASINDA SAYI URETIYOR
    else:
        tahmin=random.randrange(kucuk[-1],buyuk[0])
        print('\nTahminim :',tahmin)
        pass
        while True:#KULLANICI YONLENDIRMELERI
            user=input("""     LUTFEN TAHMINIMI DOGRULA
    YUKSELT    '+'       '-'   DUSUR
    RESET      'R'       'Q'   CIKIS
--------> :""")

            if user=='q' or user=='Q':
                print('cikiliyor... ')
                quit()
            elif user == 'r' or user == 'R' :
                print ( '\nOYUN YENIDEN BASLIYOR.....................................' , '\n' * 4)
                kucuk = [0]
                buyuk = [100]
                break
            elif user != "+" and user != "-" and user!='':
                print('....Hata lutfen + yada - giriniz......')
                continue

            else :
                if user=='-':              #- ISARETI SAYININ BUYUK OLDUGUNU GOSTERIR
                    buyuk.append(tahmin)   #BU YUZDEN BUYUK LISTESINE EKLIYORUZ
                    buyuk.sort()           #BUYUK LISTESINI EN KUCUKTEN BUYUGE DOGRU SIRALIYORUZ

                    break
                elif user=='+':            #+ ISARETI SAYININ KUCUK OLDUGUNU GOSTERIR
                    kucuk.append(tahmin)   #BU YUZDEN KUCUK LISTESINE EKLIYORUZ
                    kucuk.sort()           #KUCUK LISTESINI EN KUCUKTEN BUYUGE DOGRU SIRALIYORUZ

                    break
                elif user=='':
                    print('\n__________________TUTTUGUN SAYI {} DIR____________________\n'.format(tahmin))
                    kucuk=[0]
                    buyuk=[100]
                    print("\nOYUN YENIDEN BASLIYOR .................................... ")
                    print ( "AKLINDAN SAYI TUT ........................................ " , '\n' * 4 )
                    break
