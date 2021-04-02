# Thomas Elzinga 
# 234184
# Je kunt hier in berekenen of je inkomsten belating moet betalen.

salaris = int(input("wat is uw salaris: "))
if (salaris < 10000):
    belasting = 0
    belasting = salaris
elif (salaris < 50000):
    belasting = (salaris - 10000) / 100*30
else:
    belasting = (salaris - 50000) / 2
print("De belasting die u moet betalen is €" + str(belasting))
