# -*- coding: utf-8 -*-
'''
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.


Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
'''
import re

def get_ints_without_description(f_name):
    with open(f_name,'r') as f:
        int_dict = {}
        int_list = []
        for line in f:
            if line.startswith('interface'):
                intf = re.search(r'interface (\S+)',line).group(1)
                int_dict[intf] = ''
            elif line.startswith(' description'):
                desc = re.search(r' description (\S+)',line).group(1)
                int_dict[intf] = desc
        for line in int_dict.keys():
            if not int_dict[line]: int_list.append(line)
    return(int_list)

if __name__=='__main__':
    print(get_ints_without_description('config_r1.txt'))
