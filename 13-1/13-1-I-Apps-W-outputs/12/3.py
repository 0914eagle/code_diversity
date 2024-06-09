
def get_compressed_version(s):
    # Initialize variables
    compressed_version = []
    current_count = 1
    current_string = s[0]

    # Iterate through the string
    for i in range(1, len(s)):
        # If the current character is the same as the previous one, increment the count
        if s[i] == current_string:
            current_count += 1
        # If the current character is different from the previous one, add the current count and string to the compressed version
        else:
            compressed_version.append(str(current_count))
            compressed_version.append(current_string)
            current_count = 1
            current_string = s[i]

    # Add the last count and string to the compressed version
    compressed_version.append(str(current_count))
    compressed_version.append(current_string)

    return compressed_version

def get_min_length(s):
    # Get the compressed version of the string
    compressed_version = get_compressed_version(s)

    # Calculate the length of the compressed version
    length = 0
    for i in range(0, len(compressed_version), 2):
        length += len(compressed_version[i])
        length += len(compressed_version[i+1])

    return length

if __name__ == '__main__':
    s = input()
    print(get_min_length(s))

