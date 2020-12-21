'''
Created on 2020. 12. 21.

@author: ohsan
'''
money = [500,100,50,10,5,1]
inputMoney = 1000-int(input())
count =0
while inputMoney>0:
    for i in range(len(money)):
        if inputMoney-int(money[i])>=0:
            inputMoney-=int(money[i])
            count+=1
            break
        else :continue
print(count)