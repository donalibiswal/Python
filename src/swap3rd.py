#WAP that swap the contents of the variable without using third variable
a = 10
b = 20

print("value of a before swapping:", a)  
print("value of b before swapping:", b)  

a = a + b  
b = a - b  
a = a - b  

print("value of a after swapping:", a)  
print("value of b after swapping:", b)  
