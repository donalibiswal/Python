#print fibonacci series upto n (first 10 numbers)
num = int(input("enter a no"))
a,b = 0,1
print(a,b,end=" ")
for i in range(2,num):
    c = a+b
    print(c,end=" ")
    a,b = b,c
    print()

