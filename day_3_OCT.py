
def Is_Same_Array(array1, array2):
    if len(array1) != len(array2):
        return False


    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False
    return True

array1 =[1,2,3,4]
array2 =[1,2,3,4,]

print("array1 ::{} array2 :: {} ".format(array1,array2),Is_Same_Array(array1,array1))