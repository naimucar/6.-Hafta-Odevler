import random
tahta = ["___", "___", "___","___", "___", "___","___", "___", "___"]
kontrol_x=[" X "," X "," X "]
kontrol_o=[" O "," O "," O "]
tahmin_1 =["___"," X "," X "]
tahmin_2 =[" X ","___"," X "]
tahmin_3 =[" X "," X ","___"]
atak_1   =["___"," O "," O "]
atak_2   =[" O ","___"," O "]
atak_3   =[" O "," O ","___"]

depo=[]
cozum=[]
sira=0
cks=0
sayac=0
print ( '\n' * 5 )
print ( 1 , 2 , 3 , ' ' * 30 , tahta[0] , tahta[1] , tahta[2] , '\n' )
print ( 4 , 5 , 6 , ' ' * 30 , tahta[3] , tahta[4] , tahta[5] , '\n' )
print ( 7 , 8 , 9 , ' ' * 30 , tahta[6] , tahta[7] , tahta[8] , '\n' )
while True:




    if sira==0:


        #>>>>>>>>>>kullanici girisi ve hatalari  duzeltme


        user=input("""cikis=Q
lutfen X yazdirmak istediginiz konumu giriniz:""")

        if user=='q' or user=='Q':
            print('......GAME OVER......')
            break


        elif user.isdigit()==False or int(user)>10:
            print('lutfen 1-9 arasindaki secimi giriniz')
            continue

        elif user in depo:
            print('lutfen farkli bir sayi girin')
            continue


        else:#kullanici girisi

            depo+=[user]
            sira += 1
            tahta[int ( user ) - 1] = "X".center ( 3 )

    cozum = [[tahta[0] , tahta[1] , tahta[2]] ,
             [tahta[3] , tahta[4] , tahta[5]] ,
             [tahta[6] , tahta[7] , tahta[8]] ,
             [tahta[0] , tahta[3] , tahta[6]] ,
             [tahta[1] , tahta[4] , tahta[7]] ,
             [tahta[2] , tahta[5] , tahta[8]] ,
             [tahta[0] , tahta[4] , tahta[8]] ,
             [tahta[2] , tahta[4] , tahta[6]]]
    kazanc = [[tahta[0] , tahta[1] , tahta[2]] ,
             [tahta[3] , tahta[4] , tahta[5]] ,
             [tahta[6] , tahta[7] , tahta[8]] ,
             [tahta[0] , tahta[3] , tahta[6]] ,
             [tahta[1] , tahta[4] , tahta[7]] ,
             [tahta[2] , tahta[5] , tahta[8]] ,
             [tahta[0] , tahta[4] , tahta[8]] ,
             [tahta[2] , tahta[4] , tahta[6]]]
    print ( '\n' * 5 )
    print ( 1 , 2 , 3 , ' ' * 30 , tahta[0] , tahta[1] , tahta[2] , '\n' )
    print ( 4 , 5 , 6 , ' ' * 30 , tahta[3] , tahta[4] , tahta[5] , '\n' )
    print ( 7 , 8 , 9 , ' ' * 30 , tahta[6] , tahta[7] , tahta[8] , '\n' )

    if sira==1:

        cks=0 # ATAK kazanma icin oynama
        for d in range ( 0 , 8 ) :

            for z in kazanc:
                if atak_1 == kazanc[d] :

                    cks += 1
                    if d == 0 :
                        depo += '1'

                        tahta[0] = 'O'.center ( 3 )

                    elif d == 1 :
                        tahta[3] = 'O'.center ( 3 )
                        depo += '4'


                    elif d == 2 :
                        tahta[6] = 'O'.center ( 3 )
                        depo += '7'


                    elif d == 3 :
                        tahta[0] = 'O'.center ( 3 )
                        depo += '1'


                    elif d == 4 :
                        tahta[1] = 'O'.center ( 3 )
                        depo += '2'


                    elif d == 5 :
                        tahta[2] = 'O'.center ( 3 )
                        depo += '3'


                    elif d == 6 :
                        tahta[0] = 'O'.center ( 3 )
                        depo += '1'


                    elif d == 7 :
                        tahta[2] = 'O'.center ( 3 )
                        depo += '3'

                if cks == 1 :
                    break
                if atak_2 == kazanc[d] :

                    cks += 1
                    if d == 0 :
                        tahta[1] = 'O'.center ( 3 )
                        depo += '2'


                    elif d == 1 :
                        tahta[4] = 'O'.center ( 3 )
                        depo += '5'


                    elif d == 2 :
                        tahta[7] = 'O'.center ( 3 )
                        depo += '8'



                    elif d == 3 :
                        tahta[3] = 'O'.center ( 3 )
                        depo += '4'


                    elif d == 4 :
                        tahta[4] = 'O'.center ( 3 )
                        depo += '5'



                    elif d == 5 :
                        tahta[5] = 'O'.center ( 3 )
                        depo += '6'


                    elif d == 6 :
                        tahta[4] = 'O'.center ( 3 )
                        depo += '5'


                    elif d == 7 :
                        tahta[4] = 'O'.center ( 3 )
                        depo += '5'
                if cks == 1 :
                    break

                if atak_3 == kazanc[d] :

                    cks += 1
                    if d == 0 :
                        tahta[2] = 'O'.center ( 3 )
                        depo += '3'


                    elif d == 1 :
                        tahta[5] = 'O'.center ( 3 )
                        depo += '6'


                    elif d == 2 :
                        tahta[8] = 'O'.center ( 3 )
                        depo += '9'

                    elif d == 3 :
                        tahta[6] = 'O'.center ( 3 )
                        depo += '7'


                    elif d == 4 :
                        tahta[7] = 'O'.center ( 3 )
                        depo += '8'


                    elif d == 5 :
                        tahta[8] = 'O'.center ( 3 )
                        depo += '9'


                    elif d == 6 :
                        tahta[8] = 'O'.center ( 3 )
                        depo += '9'


                    elif d == 7 :
                        tahta[6] = 'O'.center ( 3 )
                        depo += '7'
                if cks == 1 :
                    break


        cks=0  #DEFANS      x i kontrol etme
        for d in range ( 0 , 8 ) :

            for z in cozum :

                if tahmin_1 == cozum[d] :

                    cks+=1
                    if d == 0 :
                        depo += '1'

                        tahta[0] = 'O'.center( 3 )

                    elif d == 1 :
                        tahta[3] = 'O'.center( 3 )
                        depo += '4'


                    elif d == 2 :
                        tahta[6] = 'O'.center( 3 )
                        depo += '7'


                    elif d == 3 :
                        tahta[0] = 'O'.center ( 3 )
                        depo += '1'


                    elif d == 4 :
                        tahta[1] = 'O'.center ( 3 )
                        depo += '2'


                    elif d == 5 :
                        tahta[2] = 'O'.center( 3 )
                        depo += '3'


                    elif d == 6 :
                        tahta[0] = 'O'.center( 3 )
                        depo += '1'


                    elif d == 7 :
                        tahta[2] = 'O'.center( 3 )
                        depo += '3'

                if cks==1:

                    break
                if tahmin_2 == cozum[d] :

                    cks+=1
                    if d == 0 :
                        tahta[1] = 'O'.center( 3 )
                        depo += '2'


                    elif d == 1 :
                        tahta[4] = 'O'.center( 3 )
                        depo += '5'


                    elif d == 2 :
                        tahta[7] = 'O'.center( 3 )
                        depo += '8'



                    elif d == 3 :
                        tahta[3] = 'O'.center( 3 )
                        depo += '4'


                    elif d == 4 :
                        tahta[4] = 'O'.center( 3 )
                        depo += '5'



                    elif d == 5 :
                        tahta[5] = 'O'.center( 3 )
                        depo += '6'


                    elif d == 6 :
                        tahta[4] = 'O'.center( 3 )
                        depo += '5'


                    elif d == 7 :
                        tahta[4] = 'O'.center ( 3 )
                        depo += '5'
                if cks==1:
                    break

                if tahmin_3 == cozum[d] :

                    cks+=1
                    if d == 0 :
                        tahta[2] = 'O'.center( 3 )
                        depo += '3'


                    elif d == 1 :
                        tahta[5] = 'O'.center( 3 )
                        depo += '6'


                    elif d == 2 :
                        tahta[8] = 'O'.center( 3 )
                        depo += '9'

                    elif d == 3 :
                        tahta[6] = 'O'.center ( 3 )
                        depo += '7'


                    elif d == 4 :
                        tahta[7] = 'O'.center( 3 )
                        depo += '8'


                    elif d == 5 :
                        tahta[8] = 'O'.center( 3 )
                        depo += '9'


                    elif d == 6 :
                        tahta[8] = 'O'.center( 3 )
                        depo += '9'


                    elif d == 7 :
                        tahta[6] = 'O'.center( 3 )
                        depo += '7'
                if cks == 1 :
                    break


        while cks==0:  #sart yoksa random gonderme
            a = random.randrange ( 0 , 10 )
            if str ( a ) in depo :
                continue
            else:
                tahta[int ( a ) - 1] = "O".center ( 3 )
                depo += [str ( a )]
                cks+=0

            break

        sira=0


    #kazanma kosullari
    cozum = [[tahta[0] , tahta[1] , tahta[2]] ,
             [tahta[3] , tahta[4] , tahta[5]] ,
             [tahta[6] , tahta[7] , tahta[8]] ,
             [tahta[0] , tahta[3] , tahta[6]] ,
             [tahta[1] , tahta[4] , tahta[7]] ,
             [tahta[2] , tahta[5] , tahta[8]] ,
             [tahta[0] , tahta[4] , tahta[8]] ,
             [tahta[2] , tahta[4] , tahta[6]]]
    print ( '\n' * 5 )
    print ( 1 , 2 , 3 , ' ' * 30 , tahta[0] , tahta[1] , tahta[2] , '\n' )
    print ( 4 , 5 , 6 , ' ' * 30 , tahta[3] , tahta[4] , tahta[5] , '\n' )
    print ( 7 , 8 , 9 , ' ' * 30 , tahta[6] , tahta[7] , tahta[8] , '\n' )

    for i in range(0,8):


        if kontrol_x==cozum[i]:

            print('X kazandi')
            depo = []
            sira=0
            tahta = ["___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___"]
            print ( '\n' * 5 )
            print ( 1 , 2 , 3 , ' ' * 30 , tahta[0] , tahta[1] , tahta[2] , '\n' )
            print ( 4 , 5 , 6 , ' ' * 30 , tahta[3] , tahta[4] , tahta[5] , '\n' )
            print ( 7 , 8 , 9 , ' ' * 30 , tahta[6] , tahta[7] , tahta[8] , '\n' )
            break
        elif kontrol_o==cozum[i]:
            sira=0
            print ( 'O kazandi' )
            depo = []
            tahta = ["___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___"]
            print ( '\n' * 5 )
            print ( 1 , 2 , 3 , ' ' * 30 , tahta[0] , tahta[1] , tahta[2] , '\n' )
            print ( 4 , 5 , 6 , ' ' * 30 , tahta[3] , tahta[4] , tahta[5] , '\n' )
            print ( 7 , 8 , 9 , ' ' * 30 , tahta[6] , tahta[7] , tahta[8] , '\n' )
            break

        else:
            if len(depo)>9:
                print('............Vay be...Berabere...................')
                depo = []
                sira = 0
                tahta = ["___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___"]
                print ( '\n' * 5 )
                print ( 1 , 2 , 3 , ' ' * 30 , tahta[0] , tahta[1] , tahta[2] , '\n' )
                print ( 4 , 5 , 6 , ' ' * 30 , tahta[3] , tahta[4] , tahta[5] , '\n' )
                print ( 7 , 8 , 9 , ' ' * 30 , tahta[6] , tahta[7] , tahta[8] , '\n' )
                break
