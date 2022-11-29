#Checks two adjacent values and sorts the two then moves to the next pair.
def bubble_sort(numb_list):
    size = len(numb_list)
    for i in range(size - 1):
        checker = False
        for j in range(size-1-i):
            if numb_list[j] > numb_list[j+1]:
                tmp = numb_list[j]
                numb_list[j] = numb_list[j+1]
                numb_list[j+1] = tmp
                checker = True
        if not checker:
            break
    return numb_list


lst = [12, 4, 56, 76, 3, 14, 25, 20, 29, 18]
print(bubble_sort(lst))