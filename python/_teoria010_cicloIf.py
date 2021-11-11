voto = int(input("Scrivi il tuo voto: "))
if (voto > 8):
    print("ECCELLENTE")
elif (voto >= 7) & (voto < 8): 
    print("SUFFICIENTE")     # elif = else con un altra condizione
elif(voto >= 6) & (voto < 7):
    print("SUFFICIENTE")
else:
    print("INSUFFICIENTE")