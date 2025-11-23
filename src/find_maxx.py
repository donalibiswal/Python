num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num3=int(input("enter the third number:"))
def find_max(a,b,c):
    if a>b:
        if a>c:
            print(a,"is the largest number.")
        else:
            print(c,"is the largest number.")
    elif b>a:
            if b>c:
                 print(b,"is the largest number.")
            else:
                 print(c,"is largest number.")
    elif c>a:
            if c>b:
                print(c,"is the largest number.")
            else:
                print(b,"is the largest number.")
find_max(num1,num2,num3)
