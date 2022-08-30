
def linear_search(searchlist, element):
    for value in searchlist:
        if value == element:
            return True
    return -1

def binary_search(searchlist, element):
    '''With the assumption that the list is sorted.'''
    first_index = 0
    last_index = len(searchlist) - 1
    mid_index = 0
    while first_index <= last_index:
        mid_index = (first_index + last_index) // 2
        mid_value = searchlist[mid_index]
        if element == mid_value:
            return f"The number is in index position {mid_index}"
        if element > mid_value:
            first_index = mid_index + 1
        else:
            last_index = mid_index - 1
    return -1

def binary_search_recursive(searchlist, element, start, last):
    '''To use recursion to solve the same.'''
    if last < start:
        return -1
    mid_index = (start + last) // 2
    if mid_index > len(searchlist) or mid_index < 0:
        return -1
    mid_value = searchlist[mid_index]

    if element == mid_value:
        return f"The number is in index position {mid_index}"
    if element > mid_value:
        start = mid_index + 1
    else:
        last = mid_index - 1
    return binary_search_recursive(searchlist, element, start, last)

searchlist = [4, 5, 17, 26, 49, 75, 89, 103]
# print(linear_search(searchlist, 49))
print(binary_search(searchlist, 77))
print(binary_search_recursive(searchlist, 77, 0, 2))