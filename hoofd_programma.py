####################################################
#Import functies
####################################################

from helper import onderstreep

uitvoer = onderstreep(" AANBIEDING ")
uitvoer.append("Aardbeienijs, emmertje van 5 liter : 5 €")
uitvoer.append("Slagroomn spuitbus van 1 liter : 2 €")
uitvoer.append("Nu met gratis sprinkeltjes")
print()

for el in uitvoer:
    print(el)
