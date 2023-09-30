# Find the mean,median,mode of the given numbers.

import statistics

num=int(input("Enter the total number of elements:"))
listnum=[]
for i in range(num):
    new_num=int(input("Enter the value of elements:"))
    listnum.append(new_num)

print("The mean , median,mode of the numbers will be:")

mean=statistics.mean(listnum)
print("Mean:",mean)

median=statistics.median(listnum)
print("Median:",median)

mode=statistics.mode(listnum)
print("Mode:",mode)