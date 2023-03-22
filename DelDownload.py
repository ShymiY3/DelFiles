import os, time
from send2trash import send2trash
from argparse import ArgumentParser

parser = ArgumentParser(description='Delete files in directory whiches modification date is older than 30 days')
parser.add_argument('-p', '--path',  type=str, default='', help='Path to directory to remove, default: current')
parser.add_argument('-d', '--mdays',  type=int, default=30, help='Max days without modification, default: 30')
parser.add_argument('-l', '--log',  type=str, default='', help='Path to store log, default: removing files directory')
args = parser.parse_args()

if args.path:
    PATH = fr'{args.path}'
else:PATH = os.getcwd()

DAYS = args.mdays*60*60*24
if not args.log:
    LOG = PATH
else: LOG = args.log

RemFiles = []


#try:
with open(os.path.join(LOG, 'DelFiles.log'), 'a+', encoding='UTF-8') as DelFiles:
    for file in os.listdir(PATH):
        if (time.time() > (modtime:=os.path.getmtime(os.path.join(PATH, file)))+DAYS) and file != 'DelFiles.txt':
            send2trash(os.path.join(PATH, file))
            RemFiles.append(time.strftime('%Y-%m-%d, %H:%M:%S', time.localtime(modtime)) + '\t' + file)

    DelFiles.write('\n'.join(RemFiles)+'\n')
#except:
 #  pass