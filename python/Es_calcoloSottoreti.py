#esercizio per il calcolo delle sottoreti

from ast import Num
from telnetlib import IP

def bin2dec(stringa):
    somma = 0
    for i,char in enumerate(stringa[::-1]):
        somma += int(char) * (2**i)
    return somma

def dec2bin(numero,nbit):
    bina = bin(int(numero))[2:]
    bina = "0" * (nbit-len(bina))+bina + "."
    return bina

def IP_dec2bin(IP_dec):
    bin = ""
    ip = IP_dec.split(".")
    for k in range(4):
        bin += ((dec2bin(int(ip[k]),8)))
    return bin[:-1]

def IP_bin2dec(IP_bin):
    dec = ""
    ip = IP_bin.split(".")
    for k in range(4):
        dec += str(bin2dec(ip[k])) + "."
    return dec[:-1]

def main():
    print(bin2dec("1001"))
    print(dec2bin(56,8))
    print(IP_bin2dec("10011100.00111010.11100011.10101010"))
    print(IP_dec2bin("192.168.16.3"))

if __name__ =="__main__":
    main()
