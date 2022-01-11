#stampare nomi con asterischi per privacy

f = open("./privacy.csv", "w")

def asterischi (nome):
    conta = len(nome)
    return nome[0] + (conta - 1)*"*"

def main():

    ancora = "si"
    voto = 0

    while ancora == "si":
        nome = str(input("inserisci un nome: "))
        voto = int(input("inserisci un voto: "))
        while voto <= 0:
            voto = int(input("inserisci un voto: "))


        nomePrivacy = asterischi(nome)
        f.write(f"{nomePrivacy} , {voto}\n")
        ancora = str(input("ne vuoi ancora ? (si/no): "))

    print("dati salvati su file")
    f.close()

if __name__ == "__main__":
    main()