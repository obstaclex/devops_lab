# Function for create list
def create_list():
    lst = list(map(int, input().split()))
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
