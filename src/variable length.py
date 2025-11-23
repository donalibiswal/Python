def add(*arg):
    sum=0
    for i in arg:
        sum=sum+i  #variable length arguement
    return sum
print(add(4,5))
print(add(4,5,6,7,8,9))

