def decodeer(tekst=""):
    #tekst = "header"
    lengte = len(tekst) + 4 
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()
    
def fooi_pp(bedrag, personen):
    try:
        bedrag_pp = bedrag/personen
    except:
        bedrag_pp = "??"
    return f"Elke persoon krijg {bedrag_pp} €."

def onderstreep(tekst=""):
    global uit
    uit = []
    uit.append(tekst)
    aantal = len(tekst)
    uit.append(aantal * "=")
    return uit
    
def som(inkomsten):
    return sum(inkomsten.values())




