#find the largest element in a list 
def largest_list(lst):
    largest = lst[0]
    for i in lst:
        if i > largest:
            largest = i
    return largest
print(largest_list([1, 2, 10, 12, 23]))