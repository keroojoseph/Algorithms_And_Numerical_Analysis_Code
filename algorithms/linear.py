arr = [2,3,4,5,6,7,9,10,45]

def linear_search(arr, value):

    for i in range(len(arr)):
        if (arr[i] == value):
            return i
    return -1


print("the index of value is:" ,linear_search(arr,45))