import os, time
from sys import argv
from send2trash import send2trash

PATH = fr'{argv[1]}'
DAYS = int(argv[2])*60*60*24

RemFiles = []

try:
    with open(os.path.join(PATH, 'DelFiles.log'), 'a+', encoding='UTF-8') as DelFiles:
        for file in os.listdir(PATH):
            if (time.time() > (modtime:=os.path.getmtime(os.path.join(PATH, file)))+DAYS) and file != 'DelFiles.txt':
                send2trash(os.path.join(PATH, file))
                RemFiles.append(time.strftime('%Y-%m-%d, %H:%M:%S', time.localtime(modtime)) + '\t' + file)

        DelFiles.write('\n'.join(RemFiles)+'\n')
except:
   pass