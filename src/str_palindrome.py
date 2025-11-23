#check if a string is palindrome or not
def str_palindrome(s):
    return s == s[::-1]

print(str_palindrome("helloolleh"))