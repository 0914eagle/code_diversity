

def by_length(arr):
    
    # Check if the array is empty
    if not arr:
        return []

    # Sort the array and reverse it
    sorted_arr = sorted(arr)
    reversed_arr = sorted_arr[::-1]

    # Replace each digit by its corresponding name
    names = []
    for num in reversed_arr:
        if num >= 1 and num <= 9:
            names.append(str(num))
        else:
            names.append('')

    # Replace the digits with their corresponding names
    for i in range(len(names)):
        if names[i] != '':
            names[i] = ''.join([chr(ord('A') + int(names[i]) - 1)])

    return names


