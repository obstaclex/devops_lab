def transform_string(string):
    lst = string.split(" ")
    newstring = "-".join(lst)
    return newstring


phrase = input("Enter string: ")
print(transform_string(phrase))
