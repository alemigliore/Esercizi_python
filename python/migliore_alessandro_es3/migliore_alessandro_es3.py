"""
Data la lista ip_address=["192.168.222.0/27","192,168.100.0/24","192.168.200.0/28","192.168.50.0/22"]
crea un file “mask.txt” in cui salvi le subnet mask associate a ciascun indirizzo IP.

"""

ip_address = ["192.168.222.0/27","192,168.100.0/24","192.168.200.0/28","192.168.50.0/22"]

f = open("./mask.txt", "w")

for k in range(len(ip_address)):
    x = ip_address[k]
    mask = str(f"{x[-3:]}\n")
    f.write(mask)

f.close()