i = 1
print("Welkom bij Papi Gelato.")

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
        keuze3 == ""


def overnieuw():
    bolletjes = int(input("hoeveel bolletjes wilt u?\n"))

    for i in range(bolletjes):
        i += 1
        keuzebolletje = input(f"welke smaak wilt u bolletje nummer {i} hebben? a) Aardbei, b) Chocolade c) Munt of d) Vanillie.\n")
        smaken = ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D']
        if not smaken.__contains__(keuzebolletje):
            print("dat is geen smaak")
            overnieuw()


    if bolletjes > 0 and bolletjes < 9:
        if bolletjes < 4:
            def overnieuw2():
                keuze2 = input(f"wilt u deze {bolletjes} bolletjes in een bakje of een hoorntje?\n".lower())
                if keuze2 == "bakje":
                    print(f"Oke dan krijgt u van mij een bakje met {bolletjes} bolletjes!")
                    overnieuw3()
                elif keuze2 == 'hoorntje':
                    print(f"Oke dan krijgt u van mij een hoorntje met {bolletjes} bolletjes!")
                    overnieuw3()
                else:
                    print("sorry ik heb u niet goed kunnen verstaan")
                    overnieuw2()
            overnieuw2()
        else:
            print(f"Oke dan krijgt u van mij een bakje met {bolletjes} bolletjes!")
            exit()
    elif bolletjes >= 0:
        print("Sorry, zulke grote bakken hebben we niet!")
        overnieuw()
    else:
        print("sorry dat snap ik niet.")
        overnieuw()

overnieuw()