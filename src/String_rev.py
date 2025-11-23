#reverse a string
def reverse_string(s):
    return s[::-1]

if __name__ == "__main__":
    s = input("Enter a string: ")
    print("The original string is:", s)
    print("The reversed string is:", reverse_string(s))