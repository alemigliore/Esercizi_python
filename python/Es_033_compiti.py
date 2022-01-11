#1) chiedere in input una stringa(con parentesi () [] {} )
#2) ciclo sulla stringa in cui si tolglie tutto tranne parentesi () [] {}
#3) se trovo parentesi aperta faccio PUSH e se la trovo chiusa faccio POP

def main():
    stringa = str(input("inserisci una stringa con parentesi "))

    for k in range(len(stringa)):
        if (stringa[k] == "(" ) or (stringa[k] == ")") or (stringa[k] == "[") or (stringa[k] == "]") or (stringa[k] == "{") or (stringa[k] == "["):
            stringa[k] = ""
    print(stringa)

if __name__ == "__main__" :
    main()
