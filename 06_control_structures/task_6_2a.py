# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
ip = input("Введите IP адрес: ")
try:
    ip1,ip2,ip3,ip4 = map(int,ip.split('.'))
except:
    print("Неправильный IP адрес!")
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
        else: print('unused')
