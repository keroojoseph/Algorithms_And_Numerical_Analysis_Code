arr = [1,3,5,6,8,9,10,22,33,44]

def binary_search(arr, value):
    right = len(arr) - 1
    left = 0

    while (left <= right):
        mid = (right + left) // 2
        if (arr[mid] == value):
            return mid
        elif (arr[mid] > value):
            right = mid + 1
        else:
            left = mid - 1
    return -1


print("the index of value is:", binary_search(arr, 8))

