import re

f = open('MC-OLT.csv')
olt_cout={}
for line in f.readlines():
    line = line.strip()
    city = re.findall(r'","(.+?)","\[', line)
    olt_port = re.findall(r'-\[(.+?)\]-', line)
    olt = re.findall(r'-\[\[(.+?)\]',line)
    city=city[0] if city else None
    olt_port = olt_port[0] if olt_port else None
    olt = olt[0] if olt else None
    if city not in olt_cout.keys():
        olt_cout[city]={'olt':set(),'olt_port':set()}
        olt_cout[city]['olt'].add(olt)
        olt_cout[city]['olt_port'].add(olt_port)
    else:
        olt_cout[city]['olt'].add(olt)
        olt_cout[city]['olt_port'].add(olt_port)

for city in olt_cout.keys():
    print(city)
    print(len(olt_cout[city]['olt']))
    print(len(olt_cout[city]['olt_port']))
print(olt_cout['安阳市'])



