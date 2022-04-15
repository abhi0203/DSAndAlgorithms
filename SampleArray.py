from array import *

tempArray= array("d")

daysTemp= int(input("Enter how many days temp you want "))
tempSum=0
for i in range(daysTemp):
	temp= input("Enter day "+ str(i+1) + " temperature ")
	tempArray.append(temp)

averageTemp = sum(tempArray)/ daysTemp

print("Average temp is %0.2f" % averageTemp)

daysAboveAverage=0
for i in tempArray:
	if i > averageTemp:
		daysAboveAverage+=1

print("Number of days the temp above average is %d" % daysAboveAverage)