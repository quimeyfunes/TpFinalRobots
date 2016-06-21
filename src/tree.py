import csv
from sklearn import tree

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

fileLength = file_len('train_processed_reduced.csv') - 1

trainLength = fileLength * 2 / 3


fin = open('train_processed_reduced.csv','r')
line = fin.readline()
inputNumber = len(line.strip().split(',')) - 1  


trainingSamplesX = []
trainingSamplesY = []
validate = []
validateTarget = []

lineNumber = 0

for line in fin.readlines():
	if lineNumber < trainLength:
		data = [float(i) for i in line.strip().split(',')]
		trainingSamplesX.append(data[:inputNumber])
		trainingSamplesY.append(data[inputNumber:])
		lineNumber += 1
	else:
		data = [float(i) for i in line.strip().split(',')]
		validate.append(data[:inputNumber])
		validateTarget.append(data[inputNumber:])
		lineNumber += 1


clf = tree.DecisionTreeClassifier()
print "Training..."
clf = clf.fit(trainingSamplesX, trainingSamplesY)

print "Testing..."
fout = open('tree_results.csv','w')
writer = csv.writer(fout, delimiter = ',')

header = ["realNumber", "estimated"]
writer.writerow(header)

predictedArray = clf.predict(validate)

print predictedArray

equals = 0
count = 0
for row in validateTarget:
	estimated = round(predictedArray[count])
	realNumber = row[0]

	writeRow = []
	writeRow.append(realNumber)
	writeRow.append(estimated)
	writer.writerow(writeRow)
	
	if realNumber == estimated:
		equals += 1	
	count = count + 1

print "Predicted: " + str(equals)
print "Total: " + str(len(validate))
print "Precision = " + str(float(equals)/float(len(validate)))