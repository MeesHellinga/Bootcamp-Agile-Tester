goed_getal=False
while goed_getal==False:
    a=input("Geef een waarde (geen 0) ")
    try:
        a = int(a)
        if a !=0:
            goed_getal=True
        else:
            print("Dit is geen toegestane waarde")
    except ValueError:
        print("Dat is geen getal")
print("Bedankt voor het meedoen")    