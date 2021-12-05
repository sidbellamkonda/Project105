import csv
import math

with open('dataPro106.csv', newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)
data = file_data[0]
def mean(data):
    number = len(data)
    total = 0
    for x in data:
        total += int(x)
    mean = total/number
    return mean

squarelist = []
for number in data:
    a = int(number) - mean(data)
    #Two astericks for multiplying the number a certain amount of times
    a = a**2
    squarelist.append(a)

sum = 0
for i in squarelist:
    sum = sum+i
res = sum/(len(data)-1)
standard_deviation = math.sqrt(res)
print('standard deviation = ' + str(standard_deviation))