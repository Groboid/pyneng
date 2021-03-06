# -*- coding: utf-8 -*-
'''
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
'''
import re
template = '''object network LOCAL_{}
 host {}
 nat (inside,outside) static interface service tcp {} {}
'''

def convert_ios_nat_to_asa(in_file,out_file):
    asa_list = []
    with open(in_file,'r') as f:
        for line in f:
            match = re.search(r'ip nat (\S+) source static tcp (\S+) (\S+) interface \S+ (\S+)',line)
            if match: asa_list.append(match.groups())
#        print(asa_list)
    with open(out_file,'w') as f:
        for line in asa_list:
            f.write(template.format(line[1],line[1],line[2],line[3]))
            
if __name__=='__main__':
    convert_ios_nat_to_asa('cisco_nat_config.txt','cisco_test.txt')
