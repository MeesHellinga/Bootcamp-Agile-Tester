from random import randint, choice
aantal_dozen = 5
doos_met_kat = randint(1, aantal_dozen)#doos_met_kat = toevalsgetal tussen 1 en aantal_dozen
ronde_nummer = 0
kat_gevonden = False

print("Voor je staan", aantal_dozen, "dozen, in welke doos zit de kat?")
print("Elke keer als je de kat niet vindt, verplaatst hij zich een doos naar links of naar rechts")
while not kat_gevonden == True:#zolang niet kat_gevonden
    
    doos_te_openen = int(input("In welk nummer doos zit de kat?"))#  vraag doos_te_openen aan de gebruiker
    if doos_te_openen >= 6:
        print("Er zijn maar 5 dozen!")
    elif doos_te_openen == doos_met_kat :#  als doos_te_openen gelijk aan doos_met_kat dan
        kat_gevonden = True
        ronde_nummer = ronde_nummer+1 #  verhoog aantal_pogingen
        print("Daar is de kat! Hij zat in doos nummer", doos_met_kat, "!")#    kat_gevonden ← waar
        if ronde_nummer == 1: 
            print("Je hebt de kat in", ronde_nummer, "ronde gevonden!")
        else:
            print("Je hebt de kat in", ronde_nummer, "rondes gevonden!")
    else:#  anders
        kat_gevonden = False
        ronde_nummer = ronde_nummer+1 #  verhoog aantal_pogingen
        print("In deze doos zit geen kat!")
        if ronde_nummer == 1:
            print("Je hebt", ronde_nummer, "poging gedaan")
        else:
            print("Je hebt", ronde_nummer, "pogingen gedaan") #  verhoog aantal_pogingen
        print("Probeer opmeaow!")#   melding Kat niet gevonden
        #  verplaats de kat:
        if doos_met_kat == 1:
            doos_met_kat = doos_met_kat +1
        elif doos_met_kat == 5:
            doos_met_kat = doos_met_kat -1
        else:
            doos_met_kat = (doos_met_kat+1) or (doos_met_kat-1)
print("Bedankt voor het spelen!")
from time import sleep
sleep(3)
quit()