'''
Created on 2020. 12. 21.

@author: ohsan
'''
n = int(input())
km = input().split()
costArr = input().split()
oil = 0  #몇리터 있는지
costMin=1000000000
sumCost=0
for i in range(len(km)):
    temp = int(costArr[i])
    if costMin> temp:
        costMin=temp
    sumCost += int(km[i])*costMin
print(sumCost)   
    

