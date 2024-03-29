arr = [1,2,3,4,5,9,6,8]


def max(arr):
    maxnum = arr[0]
    for i in range(len(arr)):
        if (arr[i] > maxnum):
            maxnum = arr[i]
    return maxnum

    

print(max(arr))
