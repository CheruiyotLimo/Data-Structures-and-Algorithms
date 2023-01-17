def sort_string(s):
    character_counts = [0 for i in range(0, 256)]  # assuming ASCII 256
    for c in s:
        character_counts[ord(c)] += 1 # increment the character count when seen in the string
    current_index = 0
    new_string = [] # use a list to append in constant time
    for i in range(0, 256):
        for j in range(0, character_counts[i]):
            new_string.append(chr(i)) # update the string to the current character
    return "".join(new_string)

print(sort_string("aaklsaoemdmamseawe"))