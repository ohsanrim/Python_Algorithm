'''
Created on 2020. 12. 23.

@author: ohsan
'''
n = int(input())
s=int(input())
input=input()
pn=n*2+1
res='I'+'OI'*n

count=0
for i in range(s):
    if input[i]=="I":
        if i+pn>s:
            break
        tmp=input[i:pn+i]
        if tmp==res:
            count+=1
print(count)
