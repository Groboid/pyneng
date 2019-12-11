# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
vlans = []
print_vlan = input('Введите номер VLAN: ')
with open('CAM_table.txt','r') as f:
    for line in f:
        try:
            vlan,mac,_type,port = line.split()
        except ValueError: pass
        else:
            if vlan.isdigit():
                vlans.append([int(vlan),mac,port])
vlans.sort()
for line in vlans:
    if line[0] == int(print_vlan):
        print('{:<8} {:16} {:8}'.format(line[0],line[1],line[2]))
