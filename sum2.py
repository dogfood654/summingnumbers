array1 = [1, 2, 3, 4, 5]
array2 = []
array3 = []
array4 = []
array5 = []
array6 = []

# 1d
for i in array1:
    array2.append([i])
    array3.append(i)

# 2d
for i in array1:
    for p in array3:
        if array1[i-1] < array3[p-1]:
            array2.append([array1[i-1], array3[p-1]])
            array4.append([array1[i-1], array3[p-1]])

# 3d
for i in range(len(array4)):
    for p in array3:
        if array4[i][1] < array3[p-1]:
            array2.append([array4[i][0], array4[i][1], array3[p-1]])
            array5.append([array4[i][0], array4[i][1], array3[p-1]])

# 4d
for i in range(len(array5)):
    for p in array3:
        if array5[i][2] < array3[p-1]:
            array2.append([array5[i][0], array5[i][1], array5[i][2], array3[p-1]])
            array6.append([array5[i][0], array5[i][1], array5[i][2], array3[p-1]])

# Print in vertical
for i in array2:
    print(i, end="\n")
