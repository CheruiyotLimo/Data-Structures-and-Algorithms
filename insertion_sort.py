#Just like bubble sort, we take the first element in the unsorted side of list (anchor) and find its
# correct position in the sorted side (left) of the list.
# Time complexity poor 0(n^2) but memory efficient 0(1).

def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            j -= 1
        elements[j+1] = anchor
    return elements





if __name__ == "__main__":
    elements = [12, 4, 56, 7, 23, 13, 20]
    print(insertion_sort(elements))