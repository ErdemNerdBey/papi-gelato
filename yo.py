import time

i = 1
prijsBolletjes = 1.11
prijsBakje = 0.75
prijsHoorntje = 1.25
bakje = ''
caramel = ''
slagroom = ''
prijsSprinkel = 0


def toppingVraag():
    global topping
    topping = input('Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?\n')
    if topping == 'd' or 'D':
        caramel = True
    elif topping == 'c' or 'C':
        prijsSprinkel == 0.30
    elif topping == 'b' or 'B':
        slagroom = True
    elif topping == 'a' or 'A':
        pass
    else: print('Sorry dat snap ik niet...')



print("Welkom bij Papi Gelato.")
def bonnetje():
    print('---------["Papi Gelato"]---------')
    print(f'bolletjes       {bolletjes}x  €1,11 = €{round(float(bolletjes * prijsBolletjes),2)}  ')
    if bakje:
        print(f'bakje           1 x €{prijsBakje} = €{prijsBakje}')
        if toppingVraag == 'c' or 'C':
            print(f'topping c       {bolletjes} x €{prijsSprinkel} = €{bolletjes * prijsSprinkel}\n')
            print(f'totaal                    = €{bolletjes * 1.11 + bolletjes * prijsSprinkel + prijsBakje}')
        elif bakje and slagroom == True:
            print(f'topping b           1 x € = €0.50\n')
            print(f'totaal                    = €{bolletjes * 1.11 + 0.50 + prijsBakje}')
        else:
            print(f'totaal                    = €{bolletjes * 1.11 + prijsBakje}')
    elif hoorntje:
        print(f'hoorntje        1 x €{prijsHoorntje} = €{prijsHoorntje}')
        if toppingVraag == 'c' or 'C':
            print(f'topping c       {bolletjes} x €{prijsSprinkel} = €{bolletjes * prijsSprinkel}\n')
            print(f'totaal                    = €{bolletjes * 1.11 + bolletjes * prijsSprinkel + prijsHoorntje}')
        elif hoorntje and slagroom == True:
            print(f'topping b           1 x € = €0.50\n')
            print(f'totaal                    = €{bolletjes * 1.11 + 0.50 + prijsHoorntje}')
        else:
            print(f'totaal                    = €{bolletjes * 1.11 + prijsBakje}')
    elif bakje and caramel == True:
        print(f'bakje           1 x €{prijsBakje} = €{prijsBakje}')
        print(f'topping d       1 x €0.90 = € 0,90\n')
        print(f'totaal                    = €{bolletjes * 1.11 + 0.90 + prijsHoorntje}')
    elif hoorntje and caramel == True:
        print(f'hoorntje           1 x €{prijsHoorntje} = €{prijsHoorntje}')
        print(f'topping d       1 x €0.60 = € 0.60\n')
        print(f'totaal                    = €{bolletjes * 1.11 + 0.60 + prijsHoorntje}')






def overnieuw3():
    keuze3 = input(f"wilt u nogmeer bestellen?\n".lower())
    if keuze3 == "ja":
        overnieuw()
    elif keuze3 == "nee":
        print("bedankt voor uw bestelling, tot ziens!")
        exit()
    else:
        print("sorry ik heb u niet kunnen begrijpen!")
        overnieuw3()


def overnieuw():
    global bolletjes
    bolletjes = int(input("hoeveel bolletjes wilt u?\n"))
    for i in range(bolletjes):
        i += 1
        keuzebolletje = input(f"welke smaak wilt u bolletje nummer {i} hebben? a) Aardbei, b) Chocolade c) Munt of d) Vanillie.\n")
        smaken = ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D']
        if not smaken.__contains__(keuzebolletje):
            print("dat is geen smaak")
            overnieuw()

    if 0 < bolletjes < 9:
        if bolletjes < 4:
            def overnieuw2():
                keuze2 = input(f"wilt u deze {bolletjes} bolletjes in een bakje of een hoorntje?\n".lower())
                if keuze2 == "bakje":
                    global bakje
                    bakje = True
                    print(f"Oke dan krijgt u van mij een bakje met {bolletjes} bolletjes!")
                    toppingVraag()
                    bonnetje()
                    bakje = False
                    caramel = False
                    overnieuw3()
                elif keuze2 == 'hoorntje':
                    global hoorntje
                    hoorntje = True
                    print(f"Oke dan krijgt u van mij een hoorntje met {bolletjes} bolletjes!")
                    toppingVraag()
                    time.sleep(4)
                    bonnetje()
                    hoorntje = False
                    caramel = False
                    overnieuw3()
                else:
                    print("sorry ik heb u niet goed kunnen verstaan")
                    overnieuw2()

            overnieuw2()
        else:
            global bakje
            bakje = True
            print(f"Oke dan krijgt u van mij een bakje met {bolletjes} bolletjes!")
            toppingVraag()
            time.sleep(4)
            bonnetje()
            bakje = False
            caramel = False
            overnieuw3()
    elif bolletjes >= 0:
        print("Sorry, zoveel bolletjes kunt u niet bestellen!")
        overnieuw()
    else:
        print("sorry dat snap ik niet.")
        overnieuw()

overnieuw()
