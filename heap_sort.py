
def heapify(arr, n, i):
    smallest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)
    
def heap_sort(arr):
    n = len(arr)
    for i in range(int(n/2)-1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    arr.reverse()

my_list = [3, 5, 6, 12, 1, 45, 16, 2, 10]
heap_sort(my_list)
print(my_list)