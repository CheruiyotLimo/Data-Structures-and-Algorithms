# We repeatedly find the minimum element in the list then switch it with the first element
# or move it to the sorted side of the list.
# Easy to implement and good space complexity but poor time complexity 0(n^2)

def selection_sort(arr):
    for i in range(len(arr)-1):
        min_val = arr[i]
        k = 0
        for j in range(i+1, len(arr)):
            if arr[j] <= min_val:
                min_val = arr[j]
                k = j
        if arr[i] is min_val:
            continue
        temp = arr[i]
        arr[i] = arr[k]
        arr[k] = temp
    
arr = [9, 3, 4, 1, 7, 10]
print(selection_sort(arr))
print(arr)