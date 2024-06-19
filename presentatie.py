#Import functies

from helper import *

####################################################
#Definieer functies
####################################################

def presenteer(item, aantal):
    for item, aantal in mijn_dict.items():
        print(item + " :", str(aantal) + " €")
    print (30 * "=")    
    print("totaal :", str(totaal) + " €")    

####################################################
#Run
####################################################

mijn_dict = {"vis" : 7, "vlees" : 25, "overige" : 15}
totaal = som(mijn_dict)

inkomsten = {"aardbeien-ijs-totaal" : 1000, "Vanille-ijs-totaal" : 2000, "Chocolade-ijs-totaal" : 1500, "Waterijs-totaal" : 750}
totaal_inkomsten = som(inkomsten)
mijn_dict = inkomsten
totaal = totaal_inkomsten 

