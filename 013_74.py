# Leetcode numero 74. Search a 2D Matrix


def searchMatrix(matrix, target):
    target_found = None
    for item in matrix:
        for i in item:
            if i == target:
                target_found = i

    if target_found == target:
        return True
    else:
        return False
            

#matrix = [
 #       [1,3,5,7],[10,11,16,20],[23,30,34,60]
#]
matrix = [[1]]
target = 0

call = searchMatrix(matrix, target)
print(call)
