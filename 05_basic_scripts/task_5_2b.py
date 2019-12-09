# -*- coding: utf-8 -*-
'''
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
import sys
args = sys.argv
templ = """
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}

Mask:
/{4}
{5:<8} {6:<8} {7:<8} {8:<8}
{5:08b} {6:08b} {7:08b} {8:08b}

"""
ip,mask = args[1:]
ip1,ip2,ip3,ip4 = ip.split('.')
mask_hex = '{:08x}'.format(0x100000000-2**(32-int(mask)))
ip_hex = '{:02x}{:02x}{:02x}{:02x}'.format(int(ip1),int(ip2),int(ip3),int(ip4))
ip = '{:08x}'.format(int(ip_hex,16) & int('0x'+mask_hex,16))
ip1,ip2,ip3,ip4 = [(ip[i:i+2]) for i in range(0,len(ip_hex),2)]
mask1,mask2,mask3,mask4 = [(mask_hex[i:i+2]) for i in range(0,len(mask_hex),2)]
print(templ.format(int(ip1,16),int(ip2,16),int(ip3,16),int(ip4,16),mask,int(mask1,16),int(mask2,16),int(mask3,16),int(mask4,16)))

