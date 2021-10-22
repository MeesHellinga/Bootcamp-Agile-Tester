#[lijsten] hebben een volgrode
#(tuples) hebben een structuur
#{sets} zijn niet geindexeert, maar met unieke inhoud
#meestal gebruikt voor vergelijken van verschillende sets


fruitset={'appel','kiwi','banaan'}
print(fruitset)

print('appel' in fruitset)

if 'appel' in fruitset:
    print('koekje')

for x in fruitset:
    print('fruit')
    print(x)

print(x)

aap=22

aap

set_a = {1,4,2,8}
del set_a
# print(set_a) #dit werkt dus niet, want vorige regel breekt set_a af

a={1, 2, 3}
print(a)
a.add(4) #let op de '.' om een set te bewerken
print(a)

euros={0.2,0.5,1,2}
guldens={0.05,0.1,0.25,1,2.5,5}
print(guldens.difference(euros))
print(euros.difference(guldens))

fruitset.add('sinassappel')
fruitset.update(['mandarijn','peer'])
print(fruitset)

#hierna na dictonary