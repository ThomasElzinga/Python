# Thomas Elzinga 
# 234184
import random                   
import time

doorgaan = True
aantalkeer = 0
totaal = 0 
while (doorgaan):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #Hij pakt de random letters.
    rletter = random.choice(letters)  #Hij kiest een random letter.
    print (rletter)             #Hij print de random letter.
    starttimer = time.time()    #Als de letter is geprint dan start de timer.
    letter = input()            #Je kunt hier een letter invullen
    aantalkeer = aantalkeer + 1 #Hij telt op hoevaak je iets hebt ingevuld.
    if (letter == rletter):     #Als de letter die je hebt ingevuld gelijk is aan de random letter.
        endtimer = time.time()  # Stopt de timer
        tijd = endtimer - starttimer    #Hier telt hij de tijd bij elkaar op.
        lijst = [tijd]
        totaal = totaal + tijd  #Hij telt alle tijden bij elkaar op.
        print ("De tijd =", int(tijd))            # Elkekeer als je dezelfde letter invult komt er een tijd onder te staan wat afgerond is.
    elif (letter == "q"):       # Als je q invult stopt het programma.
        print (lijst)                # 
        print ("Het gemiddelde = ", int(totaal/aantalkeer)) # Hij print je gemiddelde.

        doorgaan = False #Hij stopt de programma.
