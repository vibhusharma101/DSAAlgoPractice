
# Time complexity ( O( n) ) Space Complexity O(n)


def merge(arr1,arr2):
    mergedArray = []
    arr1Pointer =0
    arr2Pointer = 0

    while arr1Pointer<len(arr1) and arr2Pointer < len(arr2):
        if arr1[arr1Pointer]<arr2[arr2Pointer]:
            mergedArray.append(arr1[arr1Pointer])
            arr1Pointer  = arr1Pointer+1
        else:
            mergedArray.append(arr2[arr2Pointer])
            arr2Pointer  = arr2Pointer+1
            
    if arr1Pointer<len(arr1):
        for index in range(arr1Pointer,len(arr1)):
            mergedArray.append(arr1[index])
    else:
        for index in range(arr2Pointer,len(arr2)):
            mergedArray.append(arr2[index])
    
    return mergedArray



def sortArray(arr,stIndex,enIndex):
    if stIndex>=enIndex:
        return [arr[stIndex]]
    midIndex = (stIndex+enIndex)//2
    return merge(arr1  = sortArray(arr,stIndex=stIndex,enIndex=midIndex), arr2 =sortArray(arr,stIndex=midIndex+1,enIndex=enIndex))

arr = [9,1,1,2,5]

print(sortArray(arr,0,len(arr)-1))