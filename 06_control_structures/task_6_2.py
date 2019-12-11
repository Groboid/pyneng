# -*- coding: utf-8 -*-
'''
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ip = input("Введите IP адрес: ")
ip1,ip2,ip3,ip4 = map(int,ip.split('.'))
if ip1>0 and ip1<224:
    print('unicast')
elif ip1<240:
    print('multicast')
elif ip1==255 and ip2==255 and ip3==255 and ip4==255:
    print('local broadcast')
elif ip1==0 and ip2==0 and ip3==0 and ip4==0:
    print('unassigned')
else:
    print('unused')

