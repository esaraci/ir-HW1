# author: Eugen Saraci
# date  : 04/12/18


import os
import subprocess

targets = ["data/TIPSTER/TREC_VOL4/FR94"]

def rename_file(path):
    ext = path[-3:]
    if ext == ".0Z":
        os.rename(path, path[:-3] + '_0.Z')
    elif ext == ".1Z":
        os.rename(path, path[:-3] + '_1.Z')
    elif ext == ".2Z":
        os.rename(path, path[:-3] + '_2.Z')
    else:
        pass

for target_f in targets:
    for sub_f in os.listdir(target_f):
        try:
            for file in os.listdir(target_f + '/' + sub_f):
                path = target_f + '/' + sub_f + '/' + file
                rename_file(path)
        except:
            continue

os.system("uncompress data/TIPSTER/TREC_VOL4/**/**/*")
os.system("uncompress data/TIPSTER/TREC_VOL5/**/*")

