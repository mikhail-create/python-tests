import psutil
import time
import os

disk = psutil.disk_partitions()
i=0
stat_file = open("stats.dat", "a")

stat_file.write(f"@Disk @RAM\n")

def file(i, disk, ram):
    stat_file.write(f"{i}\t{disk}\t{ram}\n")


while i<10:
    disk_C = psutil.disk_usage (disk [0] [0])
    ram = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total

    file(i, disk_C.percent, ram)

    print(i)
    print ('Процент использования диска C: ', disk_C.percent)
    print ('Процент использования оперативной памяти: ', ram)
    print('==============')

    if (ram > 80):
        print('Высокая нагрузка на оперативную память')
    i = i+1
    time.sleep(1)

print("END")
os.system("termgraph stats.dat --color {yellow,magenta}")