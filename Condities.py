#if voert een set intstructies uit indien aan voorwaarden wordt voldaan
# "#" weghalen om code te laten werken
# anders vraag hij de hele tijd andere dingen

#getal = int(input("voer een getal in: "))

#if getal == 5:
#    print("Het getal is gelijk aan 5")


#Aantal_kikkers = input('Hoeveel knikkers zijn er?')
#if int(Aantal_kikkers) <=100:
 #   print("Het aantal knikkers is gelijk aan", Aantal_kikkers)

# and/or meerdere vergelijking die tegelijk 
# waar moeten zijn of waar 1 van de vergelijkingen waar moet zijn
#getal=int(input("voer een getal tussen de 1 en 10 in"))
#if getal <= 0 or getal > 10:
#    print (f"{getal} is geen toegestane waarde")

#if getal=1 or getal<=10:
#    print("goed gedaan!")
#^klopt niet

# else  voert een set instructies uit indien 
# niet aan de voorwaarden wordt voldaan

#getal=int(input("voer een getal in:")
#if getal =

#elif voert een set instructies uit indien  
# WEL aan voorwaarden wordt voldaan

#while herhaalt een set instructies zolang een conditie waar is
# sluit een waarde in die herhaalt wordt, anders blijft hij runnen
#i=0
#while i<10:
#    i=i+1
#    print ("i=", i)
#
#    j=0
#    while j<5:
#        j=j+1
#        print("j=", j)
#        j=4
#        break
#break slaat voor na de huidige iteratie van een lus 
# de verdere verwerking over, werkt alleen in while


#try:
#    g.open("brian.txt")
#    g.write("always look on the bright side!")
#except: 
#    print("er zat een fout bij het schrijven")
#finally
#    g.close()

a = input("Geef een waarde (geen 0) ")
try:
    a=int(a)
    b=100/a
    print(b)
except ValueError:
    [print("Een woord is geen waarde")]
except ZeroDivisionError:
    print("Ik zei nog zo: geen 0")
finally:
    print("Bedankt voor het meedoen!")