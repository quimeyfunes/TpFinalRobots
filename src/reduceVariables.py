import csv
#from matplotlib.mlab import PCA
from sklearn.feature_selection import VarianceThreshold
import numpy as np
 

fin = open('train_processed.csv','r')
line = fin.readline()
inputNumber = len(line.strip().split(',')) - 1  


originalDataWithoutTarget = []
originalTarget = []


for line in fin.readlines():
	data = [float(i) for i in line.strip().split(',')]
	originalDataWithoutTarget.append(data[:369])
	originalTarget.append(data[369])

print "Cantidad original de variables:" + str(len(originalDataWithoutTarget[0]) + 1)
sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
originalDataWithoutTarget = sel.fit_transform(originalDataWithoutTarget)
print "Cantidad final de variables:" + str(len(originalDataWithoutTarget[0]) + 1)


dataToWrite = []
for x in range(0,len(originalDataWithoutTarget)):
	row = originalDataWithoutTarget[x]
	row = row.tolist()
	row.append(originalTarget[x])
	dataToWrite.append(row)

print "Guardando resultado..."
fout = open('train_processed_reduced.csv','w')
writer = csv.writer(fout, delimiter=',')
writer.writerows(dataToWrite)