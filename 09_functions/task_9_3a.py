# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
def get_int_vlan_map(config_filename):
    config_f = open(config_filename,'r')
    resulta, resultt, result = {},{},{}
    for line in config_f:
        if 'interface' in line:
            _,intf = line.split()
        if 'mode access' in line:
            resulta[intf] = 1
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
    print(get_int_vlan_map('config_sw2.txt'))
