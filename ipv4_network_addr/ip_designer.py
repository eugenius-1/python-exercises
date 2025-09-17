# This program prompts the user for a network address and a subnet mask and outputs the first, last and
# broadcast addresses respectively
import math
import re

prog_flag = False

ip_octet_tab = {}
val = 0
for i in range(0, 8):
    val += int(math.pow(2, 7-i))
    ip_octet_tab[i+1] = (i+1, int(math.pow(2, 7-i)), val)

while not prog_flag:
    subnet_info = {}
    ipv4_addr = input('Enter an ipv4 network address and subnet mask separated by space or in CIDR notation: ')
    if re.search('\s', ipv4_addr):
        subnet_info['network address'] = ipv4_addr.split(' ')[0]
        nw_octets = ipv4_addr.split(' ')[0].split('.')
        nw_octets = [int(i) for i in nw_octets]
        nw_octets[3] += 1
        subnet_info['first address'] = '.'.join([str(i) for i in nw_octets])
        nw_octets[3] -= 1
        subnet_info['subnet mask'] = ipv4_addr.split(' ')[1]
        sm_octets = ipv4_addr.split(' ')[1].split('.')
        sm_octets = [int(i) for i in sm_octets]
        for num in range(len(sm_octets)):
            if sm_octets[num] != 255:
                if sm_octets[num] == 0:
                    nw_octets[num] = 255
                else:
                    for key, val in ip_octet_tab.items():
                        if sm_octets[num] == val[2]:
                            nw_octets[num] += val[1] - 1
                            break
        subnet_info['broadcast address'] = '.'.join([str(i) for i in nw_octets])
        nw_octets[3] -= 1
        subnet_info['last address'] = '.'.join([str(i) for i in nw_octets])
    else:
        subnet_info['network address'] = ipv4_addr.split('/')[0]
        nw_octets = ipv4_addr.split('/')[0].split('.')
        nw_octets = [int(i) for i in nw_octets]
        nw_octets[3] += 1
        subnet_info['first address'] = '.'.join([str(i) for i in nw_octets])
        nw_octets[3] -= 1
        sm_prefix = int(ipv4_addr.split('/')[1])
        sm_octets = []
        for i in range(0, 4):
            if sm_prefix % 8 == 0:
                if sm_prefix == 0:
                    sm_octets.append(0)
                    nw_octets[i] = 255
                else:
                    sm_octets.append(255)
            else:
                count = 0
                for key, val in ip_octet_tab.items():
                    if sm_prefix == val[0]:
                        nw_octets[i] += val[1] - 1
                        sm_octets.append(val[2])
                        count += 1
                        break
                if count == 0:
                    sm_octets.append(255)
            sm_prefix -= 8
            if sm_prefix < 0:
                sm_prefix = 0
        subnet_info['subnet mask'] = '.'.join([str(i) for i in sm_octets])
        subnet_info['broadcast address'] = '.'.join([str(i) for i in nw_octets])
        nw_octets[3] -= 1
        subnet_info['last address'] = '.'.join([str(i) for i in nw_octets])

    print('Network address: ', subnet_info['network address'])
    print('Subnet mask: ', subnet_info['subnet mask'])
    print('First usable ip address: ', subnet_info['first address'])
    print('Last usable ip address: ', subnet_info['last address'])
    print('Broadcast address: ', subnet_info['broadcast address'])
    print('\n')

    user_exec = input('Enter 0 to exit or any other key to continue: ')
    if user_exec == '0':
        prog_flag = True

