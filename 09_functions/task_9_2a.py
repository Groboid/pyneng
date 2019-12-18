# -*- coding: utf-8 -*-
'''
Задание 9.2a

Сделать копию функции generate_trunk_config из задания 9.2

Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''


trunk_mode_template = [
    'switchport mode trunk', 'switchport trunk native vlan 999',
    'switchport trunk allowed vlan'
]

trunk_config = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}

def generate_trunk_config(intf_vlan_mapping, trunk_template):
    '''
    intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
        {'FastEthernet0/12':10,
         'FastEthernet0/14':11,
         'FastEthernet0/16':17}
    access_template - список команд для порта в режиме access

    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    '''
    result = {}
    for intf,vlan in intf_vlan_mapping.items():
        intf_dic = f'{intf}'
        result[intf_dic] = []
        for line in trunk_template:
            if 'trunk allowed vlan' in line:
                result[intf_dic].append(line+f' {",".join(str(vl) for vl in vlan)}')
            else:
                result[intf_dic].append(line)
#        if psecurity != None:
#            for line in psecurity:
#                result.append(line)
    return(result)

if __name__=='__main__':
    print(generate_trunk_config(trunk_config,trunk_mode_template))

