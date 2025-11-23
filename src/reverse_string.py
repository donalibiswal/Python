def reverse_string(input_string):
    reverse_string=" "
    for char in input_string:
        reverse_string=char+reverse_string
    return reverse_string
str=input("enter a string:")
print(reverse_string(str))
