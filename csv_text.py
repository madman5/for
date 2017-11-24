# coding:utf-8
import csv
import sys, os
sys.path.append("..")
from model.dirpath import Dir_path

p = Dir_path()
path = p.dirName("Date")
filename = os.path.join(path,"date.csv")
print filename

def getcsv(filename):
	with open(filename, mode = 'rb') as f:
		csv_reader = csv.reader(f)
		for i in csv_reader:
			# print i;
			pass
	if len(i) == 3:
		a = ','.join(i).split(',')
		return tuple(a)








if __name__ == '__main__':
	getcsv(filename)
