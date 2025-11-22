def middleNode(array):
    array_length = int(len(array))
    middle = int(array_length/2)
    new = []

    for i in array:
        posicion = array.index(i)
        if i == array[middle]:
            new.append(i)
        elif posicion > middle:
            new.append(i)

    return new

arr = [1,2,3,4,5]
call = middleNode(arr)
print(call)
