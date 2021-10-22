with open("woorden.txt", "rt") as bestand_met_woorden: #opent een context manager
    aantal_regels = bestand_met_woorden.read().splitlines()
    print("Het aantal woorden in het bestand", bestand_met_woorden.name, "is", len(aantal_regels))
    a = len(bestand_met_woorden)
    print(a)
#    print(len(bestand_met_woorden))
    



#bestand_met_woorden = open("woorden.txt", "rt")
#losse_woorden=bestand_met_woorden.read().splitlines()
#print("Het aantal woorden in het bestand", bestand_met_woorden.name, "is", len(losse_woorden))

#print(lijst_met_woorden)
#lijst_met_woorden.sort()


#-->print(len(10) in bestand_met_woorden) 

#while True:
#    langste_woord = lijst_met_woorden.readline()
#    if langste_woord == None:
#        break
#    print(langste_woord)
#def langste_woord(bestand_met_woorden):
    

a = str("programmeren stom")
print(len(a))
b=a.split()
print(b)
print(len(b))

