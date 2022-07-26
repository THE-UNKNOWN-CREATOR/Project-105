from math import sqrt
import pandas as pd
import csv

def mean(list):
    lent = len(list)
    total = 0
    for i in list:
        total = total + int(i)

    return total / lent



with open("data.csv", newline="") as dt:
    reader = csv.reader(dt)
    data = list(reader)[0]

mean = mean(data)

square_list = []

for n in data:
    num = int(n) - mean
    num = num**2
    square_list.append(num)

sum = 0

for j in square_list:
    sum = sum + j

result = sum / (len(data)-1)
std_dev = sqrt(result)
print(std_dev)