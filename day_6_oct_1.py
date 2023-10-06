def sorted_arrays(array1,array2):
    result =[]
    i=0;
    j=0;
    while i< len(array1) and j<len(array2):
        if array1[i] < array2[j]:
            result.append(array1[i])
            i +=1
        else:
            result.append(array2[j])
            j += 1
    result.extend(array1[i:])
    result.extend(array2[j:])
    return result
array1=[1,3,2,4,9,22,1]
array1.sort()
array2=[2,3,4,5,6]
array2.sort()
result = sorted_arrays(array1,array2)
print(result)



