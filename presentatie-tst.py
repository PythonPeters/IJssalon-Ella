#Import functies

from helper import *

#Definieer functies

def presenteer(item, aantal):
    for item, aantal in mijn_dict.items():
        print(item, aantal)
    print (20 * "=")    
    print("totaal :",totaal)    
        
    print (item, ":", aantal)

#Run


mijn_dict = {"vis" : 7, "vlees" : 25, "overige" : 15}
totaal = som(mijn_dict)

presenteer(mijn_dict,totaal)
