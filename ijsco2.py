import time

i = 1
prijsBolletjes = 1.11
prijsBakje = 0.75
prijsHoorntje = 1.25
bakje = ''
caramel = ''
slagroom = ''
sprinkel = ''


def toppingVraag():
    global topping
    topping = input('Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?\n')
    if topping == 'd' or 'D':
        caramel = True
    elif topping == 'c' or 'C':
        sprinkel = True
    elif topping == 'b' or 'B':
        slagroom = True
    elif topping == 'a' or 'A':
        pass
    else: print('Sorry dat snap ik niet...')



print("Welkom bij Papi Gelato.")
def bonnetje():
    print('---------["Papi Gelato"]---------')
    print(f'bolletjes       {bolletjes}x  €1,11 = €{round(float(bolletjes * prijsBolletjes),2)}  ')
    if bakje and slagroom == True:
        print(f'topping b           1 x € = €0.50\n')
        print(f'totaal                    = €{bolletjes * 1.11 + 0.50 + prijsBakje}')
    elif bakje and caramel == True:
        print(f'bakje           1 x €{prijsBakje} = €{prijsBakje}')
        print(f'topping d       1 x €0.90 = € 0,90\n')
        print(f'totaal                    = €{bolletjes * 1.11 + 0.90 + prijsHoorntje}')
    elif bakje:
        print(f'bakje           1 x €{prijsBakje} = €{prijsBakje}')
        if sprinkel == True:
            print(f'topping c       {bolletjes} x €0.30 = €{bolletjes * 0.30}\n')
            print(f'totaal                    = €{bolletjes * 1.11 + bolletjes * 0.30 + prijsBakje}')
            print(sprinkel)
        else:
            print(f'\ntotaal                    = €{bolletjes * 1.11 + prijsBakje}')
    elif hoorntje and slagroom == True:
        print(f'topping b           1 x € = €0.50\n')
        print(f'totaal                    = €{bolletjes * 1.11 + 0.50 + prijsHoorntje}')
    elif hoorntje and caramel == True:
        print(f'hoorntje           1 x €{prijsHoorntje} = €{prijsHoorntje}')
        print(f'topping d       1 x €0.60 = € 0.60\n')
        print(f'totaal                    = €{bolletjes * 1.11 + 0.60 + prijsHoorntje}')
    elif hoorntje:
        print(f'hoorntje        1 x €{prijsHoorntje} = €{prijsHoorntje}')
        if sprinkel == True:
            print(f'topping c       {bolletjes} x €0.30 = €{bolletjes * 0.30}\n')
            print(f'totaal                    = €{bolletjes * 1.11 + bolletjes * 0.30 + prijsHoorntje}')
        else:
            print(f'\ntotaal                    = €{bolletjes * 1.11 + prijsBakje}')

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
