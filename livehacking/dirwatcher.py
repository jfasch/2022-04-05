import sys
import time
import os
import shutil


srcdir = sys.argv[1]
dstdir = sys.argv[2]

while True:
    time.sleep(2)
    srcfiles = os.listdir(srcdir)
    files_to_move = []
    files_not_to_move = []
    for fn in srcfiles:
        if fn.endswith('.jpg') or fn.endswith('.JPG'):
            files_to_move.append(fn)
        else:
            files_not_to_move.append(fn)
    print('files to move:', files_to_move)
    print('files not to move:', files_not_to_move)

    for fn in files_to_move:
        shutil.move(os.path.join(srcdir, fn), dstdir)
