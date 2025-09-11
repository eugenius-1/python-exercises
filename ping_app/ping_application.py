# This program uses the in-built Python OS library to ping a router
# The program prompts the user for valid domain or ip address and uses a function in the OS library to ping
# the specified domain
import os

program_flag = False

while not program_flag:
    host = input('Enter a valid ip address or domain: ')
    os.system('ping ' + host)    # ping specified host
    os.system('tracert ' + host)    # trace number of router hops to host

    user_exit = input('Enter 0 to exit or any other key to continue: ')
    if user_exit == '0':
        program_flag = True
