def isNumberThere(arr, number):
    start =0
    end = len(arr)

    while start<=end:
        mid = (start+end)//2
        if arr[mid]==number:
            return True
        elif arr[mid]>number:
            end = mid-1
        else:
            start = mid+1
    return False

arr = [1,4,7,9,10,45,99]

print(isNumberThere(arr,40))