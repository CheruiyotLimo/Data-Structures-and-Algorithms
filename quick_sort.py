
def swapper(a, b, arr):
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp

    
def hoare_partition(start, end, elements):
    pivot_index = start
    pivot = elements[pivot_index]

    # start = pivot_index + 1
    # end = len(elements) - 1
   
    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1
        
        while elements[end] > pivot:
            end -= 1 
        if start < end:
            swapper(start, end, elements)
    swapper(pivot_index, end, elements)
    return end

def elshad_partition(start, end, arr):
    pivot_index = start
    swap_index = start
    for i in range(pivot_index+1, end+1):
        if arr[i] < arr[pivot_index]:           # [12, 4, 56, 7, 23, 13, 20]
            swap_index += 1
            swapper(swap_index, i, arr)
    swapper(swap_index, pivot_index, arr)
    return swap_index

def lomuto_partition(elements):
    pivot_index = len(elements)-1
    pivot = elements[pivot_index]
     
    p_index = 0
    i = 0
    while p_index < len(elements)-1:
        while elements[p_index] <= pivot:
            p_index += 1
        i = p_index
        if i == len(elements)-1:
            break
        while elements[i] > pivot:
            if i == len(elements)-1:
                break
            i += 1
        swapper(p_index, i, elements)
    swapper(pivot_index, p_index, elements)
    return p_index


# def quick_sort(start, end, elements):
#     if start < end:
#         pi = hoare_partition(start, end, elements)
#         quick_sort(0, pi - 1, elements)
#         quick_sort(pi + 1, end, elements)

# def quick_sort(start, end, elements):
#     if start < end:
#         pi = lomuto_partition(elements)
#         quick_sort(0, pi-1, elements)
#         quick_sort(pi+1, len(elements)-1, elements)

def quick_sort(start, end, elements):
    if start < end:
        part_ind = elshad_partition(start, end, elements)
        quick_sort(start, part_ind-1, elements)
        quick_sort(part_ind +1, end, elements)
    return elements

if __name__ == "__main__":
    lst = [12, 4, 56, 7, 23, 13, 20]
    # quick_sort(0, len(lst)-1, lst)
    print(quick_sort(0, 6, lst))
    # elshad_partition(0, 6, lst)
    # print(lst)