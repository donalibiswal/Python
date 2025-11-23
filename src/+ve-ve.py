l=[10,20,-10,-50,0]
countpositive=0
countnegative=0
countzero=0
for i in l:
    if i>0:
        countpositive+=1
    elif i<0:
         countnegative+=1
    else:
        countzero+=1
print("no of +ve value is :",countpositive)
print("no of -ve value is:",countnegative)
print("no of zero value is:",countzero)
