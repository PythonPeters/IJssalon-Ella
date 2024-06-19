####################################################
#Import functies
####################################################

import csv
from helper import *
from presentatie import *

####################################################
#Run
####################################################

inkomsten = {"Aardbeien-ijs-totaal" : 1000, "Vanille-ijs-totaal" : 2000, "Chocolade-ijs-totaal" : 1500, "Waterijs-totaal" : 750}
totaal_inkomsten = som(inkomsten)
mijn_dict = inkomsten
totaal = totaal_inkomsten 

presenteer(inkomsten, totaal_inkomsten)

with open("boekhouding.csv", 'w',newline='') as csvfile:     
    for key, value in inkomsten.items():
        writer = csv.writer(csvfile, delimiter=';')  
        writer.writerow([key,value])