
def find_overlap(map1, map2):
    # Initialize a dictionary to store the frequency of each cosmic object type
    freq = {}
    for i in range(len(map1)):
        for j in range(len(map1[0])):
            if map1[i][j] not in freq:
                freq[map1[i][j]] = 0
            freq[map1[i][j]] += 1
    
    # Find the cosmic object type that appears in both maps
    common_type = ""
    for type in freq:
        if freq[type] == 2:
            common_type = type
            break
    
    # Find the row and column indices of the first occurrence of the common type in the first map
    row_ind, col_ind = 0, 0
    for i in range(len(map1)):
        for j in range(len(map1[0])):
            if map1[i][j] == common_type:
                row_ind = i
                col_ind = j
                break
    
    # Find the row and column indices of the first occurrence of the common type in the second map
    row_ind2, col_ind2 = 0, 0
    for i in range(len(map2)):
        for j in range(len(map2[0])):
            if map2[i][j] == common_type:
                row_ind2 = i
                col_ind2 = j
                break
    
    # Return the row and column indices of the overlapping section
    return row_ind, col_ind2

def main():
    # Read the input maps
    map1 = []
    map2 = []
    for i in range(int(input())):
        map1.append(input())
    for i in range(int(input())):
        map2.append(input())
    
    # Find the overlapping section
    row_ind, col_ind = find_overlap(map1, map2)
    
    # Print the row and column indices of the overlapping section
    print(row_ind, col_ind)

if __name__ == '__main__':
    main()

