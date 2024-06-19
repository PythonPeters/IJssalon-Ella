from helper import decodeer

def print_aanbieding():
    prijzen = {
        "aardbei" : 3,
        "vanille" : 4,
        "chocolade" : 5,
    }

    aanbieding = prijzen["aardbei"] * 0.8

    reclame_tekst1 = (f"Vandaag in de aanbieding : aardbei-ijs, 1 liter is slechts €{aanbieding}.")

    reclame_tekst2 = reclame_tekst1[:64]

    reclame_tekst3 = reclame_tekst2.upper()

    reclame_tekst4 = reclame_tekst3.split()

    for el in reclame_tekst4:
        if (len(el)) >= 5:
            print(el)
        else:
            print(el.lower())
            
decodeer("Aanbieding van de dag.")
print_aanbieding()
