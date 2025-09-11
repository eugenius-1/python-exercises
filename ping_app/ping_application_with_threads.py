# This program uses the concept of threading and the Threading Library to ping several hosts or routers
# simultaneously
import os
import time
import threading
import concurrent.futures

program_start = time.perf_counter()

host_number = input('Enter the number of hosts/ip addresses to be pinged: ')
host_list = []

print(f'Enter {host_number} host(s) or ip address(es):')
for num in range(int(host_number)):
    host = input()
    host_list.append(host)
print(host_list)

# TRADITIONAL IMPLEMENTATION OF THREADING
ths1_run1 = time.perf_counter()
threads = []

for host in range(len(host_list)):
    t = threading.Thread(target=lambda: os.system(f'ping {host_list[host]}'))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

ths1_run2 = time.perf_counter()

# IMPLEMENTING THREADING EFFICIENTLY WITH THREAD POOL (LESS CODE TO IMPLEMENT)
# Elements in host_list need to be formatted correctly in order to work properly with in-built map and
# os.system functions with regard to argument-parsing
host_list = ['ping ' + host for host in host_list]  # concatenating every domain in the list with ping
ths2_run1 = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(os.system, host_list)

ths2_run2 = time.perf_counter()
print('\n')
# Estimating run times of two thread process sets for comparison
print(f'Thread Set 1 Run time: {ths1_run2 - ths1_run1:.2f} second(s)')
print(f'Thread Set 2 Run time: {ths2_run2 - ths2_run1:.2f} second(s)')

program_finish = time.perf_counter()
print('\n')
print(f'Program finished in {program_finish - program_start:.2f} second(s)')  # Tracking entire program run time
