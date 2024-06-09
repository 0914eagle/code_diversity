
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

def get_minimum_length(s):
    # Get all possible compressed versions of the string
    compressed_versions = []
    for i in range(1, len(s)):
        compressed_versions.append(get_compressed_version(s[:i]))

    # Find the compressed version with the minimum length
    minimum_length = float('inf')
    for compressed_version in compressed_versions:
        length = 0
        for element in compressed_version:
            length += len(element)
        if length < minimum_length:
            minimum_length = length

    return minimum_length

if __name__ == '__main__':
    s = input()
    print(get_minimum_length(s))

