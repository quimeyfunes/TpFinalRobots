import csv
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

fileLength = file_len('train_processed.csv') - 1

trainLength = fileLength * 2 / 3


fin = open('train_processed.csv','r')
line = fin.readline()
inputNumber = len(line.strip().split(',')) - 1  


ds = SupervisedDataSet(inputNumber, 1)
validate = []

lineNumber = 0

for line in fin.readlines():
	if lineNumber < trainLength:
		data = [float(i) for i in line.strip().split(',')]
		ds.addSample(data[:inputNumber],data[inputNumber:])
		lineNumber += 1
	else:
		data = [float(i) for i in line.strip().split(',')]
		validate.append(data)
		lineNumber += 1


net = buildNetwork(inputNumber,200,100,20,5,1)
trainer = BackpropTrainer(net, ds)
print "Training..."
trainer.trainEpochs(10)

print "Testing..."
fout = open('train_processed_results.csv','w')
writer = csv.writer(fout, delimiter = ',')

header = ["realNumber", "estimated"]
writer.writerow(header)

equals = 0
for row in validate:
	estimated = round(net.activate(row[:inputNumber])[0])
	realNumber = row[inputNumber]
	row.append(estimated)
	writer.writerow(row[inputNumber:])
	if realNumber == estimated:
		equals += 1	

print "Predicted: " + str(equals)
print "Total: " + str(len(validate))
print "Precision = " + str(float(equals)/float(len(validate)))