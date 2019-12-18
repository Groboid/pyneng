# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
def get_int_vlan_map(config_filename):
    config_f = open(config_filename,'r')
    resulta, resultt, result = {},{},{}
    for line in config_f:
        if 'interface' in line:
            _,intf = line.split()
        if 'access vlan' in line:
            _,_,_,vlan = line.split()
            resulta[intf] = int(vlan)
        if 'trunk allowed vlan' in line:
            _,_,_,_,vlan = line.split()
            print(vlan)
            resultt[intf] = []
            resultt[intf] = list(map(int,vlan.split(',')))
    return(resulta,resultt)

if __name__=='__main__':
    print(get_int_vlan_map('config_sw1.txt'))
