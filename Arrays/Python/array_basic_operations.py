
def removeElementFromAnIndex(arr,index):
    for index in range(index,len(arr)-1):
        arr[index] = arr[index+1]
    arr[len(arr)-1] = 0
    return arr


arr = [1,2,3,4,5]

# time complexity of removing from middle is O(n)
print(removeElementFromAnIndex(arr,2))

# time complexity of adding in middle is O(n)
# time complexity of adding or removing from start or end is O(1)

