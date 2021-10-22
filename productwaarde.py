def product(factor1,factor2):
    resultaat=factor1*factor2
    return resultaat

print("Unittest van 'product'")
assert product(9,3)==27, "Brekening van 'product'bevat een fout"
assert product(0,0)==0,"fout bij berekenen 0 waarde"
assert product(1000,1000)==1000000, "fout bij berekenen grote waarde"
