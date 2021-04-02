#Thomas Elzinga
# 234184 

# als er geen 0 ingevoerd word gaat het programma steeds door.
# Maar als er wel een 0 word ingetypt stopt de programma en rekent de gemiddelde uit

# getal Inlezen
doorgaan = True
aantal = 0
totaal = 0
 
# Een loop zodat de vraag medere keer word gevraagd
while (doorgaan == True):
    getal = int(input("Vul een getal in: "))
    # Het optellen van de ingevulde getallen
    totaal = totaal + getal
    aantal = aantal + 1
    # De loop stoppen als er 0 word ingevuld
    if (getal == 0):
        doorgaan = False
        aantal = aantal - 1
    # Het (delete en) de waarschuwing voor een -getal
    elif (getal < 0):
        #del getal
        print("Alleen getallen boven de 0 invullen.")
    
    # Het printen van de uitkomst en het delen van het totaal
print("Je gemiddelde is: " + str(totaal/aantal))