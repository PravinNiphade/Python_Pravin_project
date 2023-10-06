def sigle_occurence(arrays):
    result =0
    for i in arrays:
        result ^= i
    return result

arrays = [10,10,20,30,40,20,30,40,50]
result = sigle_occurence(arrays)
print("The number appears only once {}".format(result))