# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
import ipaddress
import subprocess

def ping_ip_addresses(ips):
    print('Testing ')
    ip1,ip2 =[],[]
    for ip in ips:
        reply = subprocess.run(['ping','-c','4','-n',ip],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        if reply.returncode == 0:
            ip1.append(ip)
        else:
            ip2.append(ip)
        print('.',end='',flush=True)
    return(ip1,ip2)

if __name__=='__main__':
    ip_list = ['8.8.8.8','8.8.4.4','192.168.10.10','127.0.0.1','10.10.10.10']
    print(ping_ip_addresses(ip_list))
