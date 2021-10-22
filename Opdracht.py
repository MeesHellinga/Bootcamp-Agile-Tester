# Spelen met woorden
# Wat Python code om alvast aan de slag te kunnen
# Het bestand 'woorden.txt.zip' staat op deze pagina

bestand_met_woorden = open("woorden.txt", "rt") # alleen-lezen van tekst
#lijst_met_woorden = bestand_met_woorden.readlines()
lijst_met_woorden = bestand_met_woorden.read().splitlines()
bestand_met_woorden.close()

aantal_woorden = 0
for woord in lijst_met_woorden:
  #print(woord)
  aantal_woorden = aantal_woorden + 1
  lijst_met_woorden.sort(reverse=True, key=len)
  print(lijst_met_woorden[0])
  
  
  #x=str.count(bestand_met_woorden)
  

print(aantal_woorden)

bestand_met_woorden.close()
#Hoeveel woorden hebben meer dan X tekens?
#Wat is het meeste aantal letters voor 1 woord in lijst
#Welke woord heeft dat aantal letters?