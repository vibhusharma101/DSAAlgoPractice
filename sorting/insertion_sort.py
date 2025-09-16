def sortArray (arr):
    for index in range(0,len(arr)):
        print(arr[index])
        for innerIndex in range(index-1,-1,-1):
            if arr[index]<arr[innerIndex]:
                arr[index], arr[innerIndex] = arr[innerIndex] , arr[index]
            else:
                break
    return arr

arr = [2,4,1,3,2]

print(sortArray(arr))