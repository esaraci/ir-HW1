#! usr/env/python

import os

targets = ["TIPSTER/TREC_VOL4/FR94"]

def rename_file(path):
	ext = path[-3:]
	if ext == ".0Z":
		os.rename(path, path[:-3] + '-0.z')
	elif ext == ".1Z":
		os.rename(path, path[:-3] + '-1.z')
	elif ext == ".2Z":
		os.rename(path, path[:-3] + '-2.z')
	else:
		pass


for target_f in targets:
	for sub_f in os.listdir(target_f):
		try:
			for file in os.listdir(target_f + '/' + sub_f):
				path = target_f + '/' + sub_f + '/' + file
				print(path)
				rename_file(path)
		except:
			continue

