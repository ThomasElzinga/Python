# Thomas Elzinga
# 234184

leeftijd = int(input("Vul uw leefijd in: ")) #hier vraagt hij de leeftijd.


vakantiedagen = 25  # Vaste vakantiedagen

if (leeftijd < 45): # als de leeftijd onder de 45 is print hij de aantal vakantiedagen
    print ("U heeft recht op" , vakantiedagen, "vakantie dagen") 
elif (leeftijd < 56): # als de leeftijd onder de 56 invult print hij daantal +1
    vakantiedagen = vakantiedagen + 1
    print ("U heeft recht op" , vakantiedagen, "vakantie dagen")
elif (leeftijd < 68): # als je leeftijd onder de 68 invult print hij aantal + 2
    vakantiedagen = vakantiedagen + 2
    print ("U heeft recht op" , vakantiedagen, "vakantiedagen")

adienstjaren = int(input("Vul de aantaldienstjaren in: ")) #Hier vraagt hij de aantaldienstjaren


if (adienstjaren < 26): # Als je onder de 26 jaar hebt gewerkt print hij dat je geen extra dagen krijgt.
    print("U heeft geen recht op extra vakantie dagen." ,vakantiedagen, "vakantiedagen")
elif (adienstjaren < 40): # als je onde de 40 bent print hij dat je 2 extra dagen krijgt.
    vakantiedagen = vakantiedagen + 2
    print ("U heeft recht op 2 extra vakantie dagen u heeft nu" , vakantiedagen, "vakantiedagen")
elif (adienstjaren < 68): # als je onder de 68 bent print hij dat je 5 extra dagen krijgt.
    vakantiedagen = vakantiedagen + 5
    print ("U heeft recht op 5 extra vakantie dagen u heeft nu" , vakantiedagen, "vakantiedagen")
