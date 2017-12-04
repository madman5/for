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
	rows=[]
	with open(filename, mode = 'rb') as f:
		csv_reader = csv.reader(f,delimiter=',',quotechar='|')
		next(csv_reader,None)
		for i in csv_reader:
			rows.append(i)
	print rows







if __name__ == '__main__':
	getcsv(filename)
