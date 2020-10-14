# Read data file
filename = "data/wxobs20170821.txt"
datafile = open(filename, 'r')

print(datafile.readline())
print(datafile.readline())
print(datafile.readline())
print(datafile.readline())

data = datafile.read()

datafile.close()

#print(data)
#print("data")

with open(filename,'r') as datafile:
    data = datafile.read()

#print(data)
print(type(data))
