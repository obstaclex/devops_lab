# Function for create list
def create_list():
    lst = []
    n = input("Enter number of element:")
    try:
        val = int(n)
        for i in range(val):
            element = input("Enter {} element:".format(i + 1))
            lst.append(element)
    except ValueError:
        try:
            val = float(n)
            print("Input is not a int. It's a float")
        except ValueError:
            print("Input is not a int. It's a string")
    return lst


# Create two list
list1 = create_list()
list2 = create_list()


# Create dictionary from 2 list
def create_dict(a, b):
    dct = {}
    if len(a) - len(b) != 0:
        for i in range(len(a) - len(b)):
            b.append(None)
        for j in range(len(a)):
            dct[a[j]] = b[j]
        return dct


# Print dictionary
dct1 = create_dict(list1, list2)
print(dct1)
