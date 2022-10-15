#!/usr/bin/python3
from sys import argv
from os import walk
from os.path import isfile, join
all  = next(walk('.'))[1]    # get list of all directory in '.'
lall = len(all)

def usage():
    print('USAGE')
    print('kstat.py      # summary')
    print('kstat.py 2    # show folders with missing 2')
    print('kstat.py 2 4  # show folders with missing 2 or 4')
    exit(0)

argv = argv[1:]
argc = len(argv)
if argc == 0:
    # show all summary for all
    argv = [str(i) for i in range(1,9)]
else:
    if argv[0] == '-h':
        usage()
showmissing = argc>0
d = 0  # global counter
for e in argv:
    c = 0   # counter
    
    for user in all:
        fname = join(user, user + '-e%s.txt'%e)
        if (isfile(fname)):
            c += 1
        else:
            if showmissing:
                print(user)
    if not(showmissing):
        print('exercise %s done: %3d / %3d  %3.0f%%' % (e, c, lall, 100*c/lall))
    d += c
# overall summary
print('--------------------------------')
print('ALL done:       %3d /%3d  %3.0f%%' % (d, len(argv)*lall, 100*d/(len(argv)*lall)))

