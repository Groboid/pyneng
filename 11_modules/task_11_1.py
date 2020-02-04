# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое файла в строку.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

В словаре интерфейсы должны быть записаны без пробела между типом и именем. То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
def parse_cdp_neighbors(command_output):
    dict_r = {}
    parse = False
    for line in command_output:
        if 'show cdp neighbors' in line:
            main_r = line.split('>')[0]
        if parse:
#            print(line.split())
            r,f1,f2,*_,f3,f4 = line.split()
            dict_r[(main_r,f1+f2)] = (r,f3+f4)
        if 'Device ID' in line: parse = True
    return dict_r

if __name__ == '__main__':
    f = open('sh_cdp_n_sw1.txt','r')
    print(parse_cdp_neighbors(f.readlines()))
