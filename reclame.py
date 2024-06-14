#Import Functies
#########################

from algemene_functies import mijn_functie_2

#Aanmaken functies
#########################

def aanbieding_1(smaak, prijs, korting):
    korting = prijs - (korting * prijs)
    #print(korting)
    print(f"Vandaag in de aanbieding : emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} € nu voor " + str(korting) + " €")

def inkomsten_totaal(inkomsten):
    return sum(inkomsten)

def laag_hoog (mijn_lijst):
    global hoog
    global laag
    hoog = max(mijn_lijst[0:7])
    laag = min(mijn_lijst[0:7])
    return([laag, hoog])

def gemiddeld (mijn_lijst):
    aantal = len(mijn_lijst)
    aantal = aantal - 1
    gemiddelde = totaal / aantal
    return(gemiddelde)

def meervoudig (invoer_lijst):
    mijn_lijst = invoer_lijst
    laag_hoog (mijn_lijst)
    return([laag, hoog])

def combinatie(korte_lijst):
    mijn_functie_2(korte_lijst)
    
    
#Vragen huiswerk
#########################
    
aanbieding_1("aardbei", 4, 0.1)
inkomsten = ([220, 430, 125, 160, 205, 90, 345, 9])
invoer_lijst = ([10, 5, 3, 2, 1, 2, 9])
totaal = inkomsten_totaal(inkomsten[0:7])
btw = inkomsten_totaal(inkomsten[7:])
btw = btw * 0.01 * totaal
mijn_lijst = inkomsten

#On screen
#########################

print(f"Het totaal van alle inkomsten van deze week is {totaal} €, waarover het bedrag {btw} € btw dient betaald te worden")
print(f"Hoogste en laagste waarde : {laag_hoog(mijn_lijst)}")
print(f"De gemiddelde inkomsten van deze week zijn {gemiddeld(mijn_lijst)} €")
print(meervoudig(invoer_lijst))
mijn_functie_2(100,20)