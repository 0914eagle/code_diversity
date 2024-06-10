
def get_matching_section(map1, map2):
    # Initialize a dictionary to store the frequency of each cosmic object type in map1
    freq1 = {}
    for row in map1:
        for char in row:
            if char not in freq1:
                freq1[char] = 1
            else:
                freq1[char] += 1
    
    # Initialize a dictionary to store the frequency of each cosmic object type in map2
    freq2 = {}
    for row in map2:
        for char in row:
            if char not in freq2:
                freq2[char] = 1
            else:
                freq2[char] += 1
    
    # Find the common cosmic object types between map1 and map2
    common_objects = []
    for obj in freq1:
        if obj in freq2 and freq1[obj] == freq2[obj]:
            common_objects.append(obj)
    
    # Find the first occurrence of the common cosmic object types in map1 and map2
    i, j = 0, 0
    for row in map1:
        for char in row:
            if char in common_objects:
                i = map1.index(row) + 1
                j = row.index(char) + 1
                break
        if i != 0 and j != 0:
            break
    
    return i, j

def main():
    map1 = [input() for _ in range(int(input()))]
    map2 = [input() for _ in range(int(input()))]
    i, j = get_matching_section(map1, map2)
    print(i, j)

if __name__ == '__main__':
    main()

