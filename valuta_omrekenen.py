# Thomas Elzinga.
# 234184.
EUR = 0.8422                                                                            # Valuta nu.
USD = 1.1874 
GBP = 0.857679
RUB = 74.9470                                                                           # Valuta nu.

def valutaberekenen():                                                                  # Maakt een functie.
    
    gekozenvaluta = input("Kies een valuta \nEUR\nUSD\nGBP\nRUB:")                              # Vraagt waar naartoe je wilt berekenen.
    print ()                                                                            # Hij print een lege lijn.
    print("U betaalt met:",gekozenvaluta)                                               # Hij print wat je hebt gekozen. 
    naar = input("Naar waar wil je het berekenen?\nrub\neur\ngbp\nusd:")
    
    if gekozenvaluta.lower() == "usd":                                                       # Als het gelijk is aan USD dan gaat hij vreder.
        hoeveel = (float(input("Hoeveel dollar wil je veranderen?\n")))                 # vraagt hoeveel je wil veranderen
        if naar.lower() == "eur":                                                       # als je eur kiest gaat hij het berekenen
            print(hoeveel, "dollar is", round(hoeveel*EUR, 2), "Euro.\n") 
        elif naar.lower() == "rub":
            print(hoeveel, "dollar is", round((hoeveel)*74.9470, 2), "rubles.")
        elif naar.lower() == "gbp":
            print(hoeveel, "dollar is", round((hoeveel)*0.857679, 2   ), "ponden.")

    if gekozenvaluta.lower() == "eur":  
        hoeveel = (float(input("Hoeveel euro wil je veranderen?\n")))                                               # Als het gelijk is aan EUR dan gaat hij vreder.
        if naar.lower() == "usd":         # Vraagt welk bedrag je wilt berkenen.
            print(hoeveel, "euro is", round(hoeveel * USD, 2), "Dollars.\n")
        elif naar.lower() == "rub":
            print(hoeveel, "euro is", round((hoeveel)*74.9470, 2 ), "rubles")
        elif naar.lower() == "gbp":
            print(hoeveel, "euro is", round((hoeveel)*0.857679, 2   ), "ponden.")

    
    if gekozenvaluta.lower() == "rub":
        hoeveel = (float(input("Hoeveel roebel wil je veranderen?\n")))
        if naar.lower() == "usd":         # Vraagt welk bedrag je wilt berkenen.
            print(hoeveel, "roebel is", round(hoeveel * USD, 2), "Dollars.\n")
        elif naar.lower() == "eur":
            print(hoeveel, "roebel is", round((hoeveel)*0.8422, 2 ), "euro")
        elif naar.lower() == "gbp":
            print(hoeveel, "roebel is", round((hoeveel)*0.857679, 2   ), "ponden.")
    
    if gekozenvaluta.lower() == "gbp":
        hoeveel = (float(input("Hoeveel pond wil je veranderen?\n")))
        if naar.lower() == "usd":        
            print(hoeveel, "pond is", round(hoeveel * USD, 2), "Dollars.\n")
        elif naar.lower() == "eur":
            print(hoeveel, "pond is", round((hoeveel)*0.8422, 2 ), "euro")
        elif naar.lower() == "rub":
            print(hoeveel, "pond is", round((hoeveel)*74.9470 , 2   ), "roebel.")



valutaberekenen()                                                                # Eindigt functie.