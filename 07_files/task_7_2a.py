# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']
import sys
args = sys.argv
f = open(args[1],'r')
for line in f:
    doprint = True
    for ign in ignore:
        if ign in line:
            doprint = False
    if not line[0]=='!' and doprint:
        print(line.strip())
