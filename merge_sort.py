def breaker_of_chains(arr):
    if len(arr) <= 1:
        return
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    breaker_of_chains(left)
    breaker_of_chains(right)
    merge_two_sorted_lists(left, right, arr)

def merge_two_sorted_lists(a, b, arr):
    i = j = k = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            arr[k] = a[i]
            i += 1
            k += 1
        else:
            arr[k] = b[j]
            j += 1
            k += 1
    while i < len(a):
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len(b):
        arr[k] = b[j]
        j += 1
        k += 1



if __name__== "__main__":
    a = [2, 9, 10, 34, 7, 4, 13, 20, 17]
    breaker_of_chains(a)
    print(a)