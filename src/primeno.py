num=int(input("enter a positive number:"))
def is_prime(num):
    if num<=1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
        else:
            return True
print(is_prime(num))
