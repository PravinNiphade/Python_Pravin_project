

def find_first_occurence(array1,array2):
    for i, element in enumerate(array1):
        if element == array2:
            return i
    return -1

array1=[1,2,3,4,2,3,4]
array2 = 4

result = find_first_occurence(array1,array2)

if result != -1:
    print("Value {}  present in  index :: {}  ".format(array2,result))
else:
    print("not present in given array")