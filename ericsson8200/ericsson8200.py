import http.client, os

parametros = []

dir_path = os.path.dirname(os.path.abspath(__file__)) #Upload the parameters from the .txt file
file_path = dir_path + r"\parametros.txt"
file = open(file_path, "r")
for line in file:
    parametros.append(line.strip())

frecuencia = parametros[0]
BISS = parametros[1]

urls = ["ip-address-from-primary-IRD", "ip-address-from-backup-ird"] #Use the IP of the IRD'S
for url in urls:
    conn = http.client.HTTPConnection(url)
    payload = "cgi=config&%24m=set&%24target=tcf%3Fcgi%3Dshow%26%2524path%3D%2FInput%2FSAT%2520Input%2FInput%25201%2520%2528L-band%2529&%24path=%2FInput%2FSAT+Input%2FInput+1+%28L-band%29&LNB+LO+Frequency=10750.000&Satellite+Frequency=" + frecuencia + "&Symbol+Rate=3.710000&Search+Mode=AUTO&Search+Range=3710&Modulation+Mode=AUTO&LNB+Power=OFF&LNB+22+kHz=ENABLE&LNB+22+kHz_check=on&Spectral+Sense=AUTO&Mapping+Mode+%28S2+only%29=MEAN+POWER&Roll+Off=20%25&Gold+Seq+N+%28S2+only%29=0&Gold+Seq+2=0&Gold+Seq+3=0&Gold+sequence+selelction+mode=SEARCH"
    headers = {"Content-type": "application/x-www-form-urlencoded; charset=UTF-8"}
    conn.request("POST", "/tcf", body=payload, headers=headers)
    ans = conn.getresponse()
    print(f"{ans.status} - {ans.reason}")
    data = ans.read()

    conn = http.client.HTTPConnection(url)
    payload = "cgi=config&%24m=set&%24target=tcf%3Fcgi%3Dshow%26%2524path%3D%2FCA&%24path=%2FCA&Over+Air+Control=Disable&Over+Air+Extd+Carrier+Timeout=Disable&Decrypt+Components+Follow+Decode=False&Enable+Service+Limiting=False&Select+Value+for+service+limit=60&Force+CAM+Voltage=False&CAM+Enable+Burst+Mode=False&BISS+Mode=MODE+1&BISS+Key=" + BISS + "&User+One=**************&User+Two=**************"
    headers = {"Content-type": "application/x-www-form-urlencoded; charset=UTF-8"}
    conn.request("POST", "/tcf", body=payload, headers=headers)
    ans = conn.getresponse()
    print(f"{ans.status} - {ans.reason}")
    data = ans.read()

print(f"\nScript ejecutado... frecuencia {frecuencia} - BISS {BISS}")
while True:
    flag = input("Presione una tecla para salir:")
    if flag != None:
        break
    else:
        pass