def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        merge(arr, left, right)
    return arr

def merge(arr, left, right):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j = j + 1
        k = k + 1


def binarySearch(arr, value):

    right = len(arr) - 1
    left = 0

    while (left <= right):
        mid = (left + right) // 2

        if (arr[mid] == value):
            return mid
        
        if (arr[mid] > value):
            right = mid - 1
        else:
            left = mid + 1
    return -1
# Testing the code

unsortedArr = [3, 7, 6, -10, 1, 23.5, 55, 4]
sortedArr = mergeSort(unsortedArr)
print("Sorted array:", mergeSort(unsortedArr))

value = 3
result = binarySearch(sortedArr, value)
if(result != -1):
    print("the value ", value, " is exsit in index ", result , " of my array")
else:
    print("not exsit")

