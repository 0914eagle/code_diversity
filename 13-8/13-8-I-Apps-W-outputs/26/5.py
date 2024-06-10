
def find_matching_section(map1, map2):
    # Initialize a dictionary to store the frequency of each character in the first map
    freq1 = {}
    for row in map1:
        for char in row:
            if char not in freq1:
                freq1[char] = 1
            else:
                freq1[char] += 1
    
    # Initialize a dictionary to store the frequency of each character in the second map
    freq2 = {}
    for row in map2:
        for char in row:
            if char not in freq2:
                freq2[char] = 1
            else:
                freq2[char] += 1
    
    # Find the matching section by comparing the frequencies of the characters in the two maps
    for i in range(len(map1)):
        for j in range(len(map2[0])):
            if freq1 == freq2:
                return i, j
    
    # If no matching section is found, return -1, -1
    return -1, -1

def main():
    # Read the input maps
    n, m = map(int, input().split())
    map1 = [input() for _ in range(n)]
    map2 = [input() for _ in range(m)]
    
    # Find the matching section
    i, j = find_matching_section(map1, map2)
    
    # Print the output
    print(i, j)

if __name__ == '__main__':
    main()

