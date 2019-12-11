# -*- coding: utf-8 -*-
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ip_correct = False
while not ip_correct:
    ip = input("Введите IP адрес: ")
    ip_correct = True
    try:
        ip1,ip2,ip3,ip4 = map(int,ip.split('.'))
    except:
        print("Неправильный IP адрес!")
        ip_correct = False
    else:
        if ip1>0 and ip1<224:
            print('unicast')
        elif ip1<240:
            print('multicast')
        elif ip1==255 and ip2==255 and ip3==255 and ip4==255:
            print('local broadcast')
        elif ip1==0 and ip2==0 and ip3==0 and ip4==0:
            print('unassigned')
        else:
            if ip1<0 or ip1>255 or ip2<0 or ip2>255 or ip3<0 or ip3>255 or ip4<0 or ip4>255:
                print("Неправильный IP адрес!")
                ip_correct = False
            else: print('unused')
