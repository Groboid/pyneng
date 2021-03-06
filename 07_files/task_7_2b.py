# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']
import sys
args = sys.argv
f = open(args[1],'r')
f2 = open('config_sw1_cleared.txt','w')
for line in f:
    doprint = True
    for ign in ignore:
        if ign in line:
            doprint = False
    if doprint:
        f2.write(line)
