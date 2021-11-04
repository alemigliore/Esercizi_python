"""Crea un programma in Python in cui assegni una parola di almeno 8 lettere a una variabile stringa 
e poi stampi tutta la parola con un carattere ? al posto della terza lettera."""

stringa= "ciao e buona notte"
print(stringa)
stringa_nuova=stringa[:3]+"?"+stringa[4:]
print(stringa_nuova)