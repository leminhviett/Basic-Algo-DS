##############################################################
def merge(array, p, q, n):
    #sorted array[p ->q] merge with sorted array[q+1 -> n]
    l, r = [], []
    for i in range(p, q+1):
        l.append(array[i])
    for i in range(q + 1, n+1):
        r.append(array[i])
    cursor_l, cursor_r = 0, 0
    cursor = p
    while(cursor_l < len(l) and cursor_r < len(r)):
        if(l[cursor_l] < r[cursor_r]):
            array[cursor] = l[cursor_l]
            cursor_l += 1
        else:
            array[cursor] = r[cursor_r]
            cursor_r += 1
        cursor += 1
    while(cursor_l < len(l)):
        array[cursor] = l[cursor_l]
        cursor_l += 1
        cursor += 1
    while (cursor_r < len(r)):
        array[cursor] = r[cursor_r]
        cursor_r += 1
        cursor += 1

# testMerge = [1,3,9,10, 5, 8, 20]
# merge(testMerge, 0, 3, 6)
# print(testMerge)

def mergeSort(array,i, j):
    if(i == j):
        return
    temp = (i+j)//2
    mergeSort(array, i, temp) #inclusive both sides
    mergeSort(array, temp + 1, j)
    merge(array, i, temp, j)

# testMergeSort = [200, 1,2,9,-5,10,20,8,100,9,0]
# mergeSort(testMergeSort, 0, len(testMergeSort) - 1)
# print(testMergeSort)
###################################################################

def partition(array, i, j):#inclusive
    val = array[i]
    h = i #index of array[i] finally
    for k in range(i+1, j + 1):
        if(array[k] < val):
            h += 1
            temp = array[h]
            array[h] = array[k]
            array[k] = temp
    temp = array[h]
    array[h] = val
    array[i] = temp
    return h

testPartion = [5,1,2,9,40,-5]
partition(testPartion, 0, len(testPartion)-1)
print(testPartion)

def quickSort(array, i, j):#inclusive
    if(i < j):
        h = partition(array, i, j)
        quickSort(array, i, h-1)
        quickSort(array, h + 1, j)

testQuicksort = [5,1,2,-4,3,10,20,-3]
quickSort(testQuicksort, 0, len(testQuicksort) - 1)
print(testQuicksort)
