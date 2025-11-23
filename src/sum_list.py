#find the sum of a list
def sum_list(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum
print(sum_list([1,2,3,4,5]))
