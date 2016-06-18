import csv
from random import shuffle

fin = open('train.csv','r')
fout = open('train_processed.csv','w')
writer = csv.writer(fout, delimiter=',')

# Header
line = fin.readline()
writer.writerow(line.strip().split(',')[1:371])

satisfiedClients = []
notSatisfiedClients = []

print "Comienzo del procesamiento..."

for line in fin.readlines():
	#En data saco la columna de ID
	data = [x for x in line.strip().split(',')[1:371]]
	#Si el target es 1 son clientes no satisfechos, si es 0 son satisfechos
	if data[369] == "1":
		notSatisfiedClients.append(data)
	elif data[369] == "0":
		satisfiedClients.append(data);

# Tomo la misma cantidad de ambos conjuntos
shuffle(satisfiedClients)
satisfiedClients = satisfiedClients[:len(notSatisfiedClients)]

# Se escriben en el archivo aleatoriamente
toWrite = satisfiedClients + notSatisfiedClients
shuffle(toWrite)
writer.writerows(toWrite)

print "Clientes satisfechos: " + str(len(satisfiedClients)) + " Clientes no satisfechos: " + str(len(notSatisfiedClients))
print "Procesamiento finalizado"