'''
Created on 2020. 12. 19.

@author: ohsan
'''

a=[]
for i in range(9):
    a.append(int(input()))
a.sort()
sumV=sum(a)
for i in range(9):
    for k in range(i,9):
        temp = a[i]+a[k]
        if sumV-temp==100 :
            for j in range(9):
                if j==i or j==k:continue
                else :
                    print(a[j])
            exit()
        
             
             
