
array1 = [1,2,3,4,5]
user_input = input("enter a number :: ")
user_input = int (user_input)
def Is_present(array1,user_input):

    for i in range(len(array1)):
        if array1[i] == user_input:
            return True
    return False
print(Is_present(array1,user_input))