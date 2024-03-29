def matrix_mul (arr, arr2):
    arr3 = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr2[0])):
            for k in range(len(arr2)):
                arr3[i][j] += (arr[i][k] * arr[k][j])
    return arr3

arr = [[1,2,3,4],[1,4,5,6]]
arr2 = [[1,2,3,4],[1,4,5,6]]

result = matrix_mul(arr, arr2)
for i in result:
    print(i)