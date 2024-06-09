
def read_input():
    n, m = map(int, input().split())
    mark = [input() for _ in range(n)]
    return n, m, mark

def f1(n, m, mark):
    # Count the number of '#' in the mark
    num_hashes = sum(line.count('#') for line in mark)
    
    # Check if the number of '#' is even
    if num_hashes % 2 == 0:
        return num_hashes // 2
    
    # If the number of '#' is odd, check if the mark can be formed by stamping the stamp twice
    for i in range(n):
        for j in range(m):
            if mark[i][j] == '#':
                # Check if the mark can be formed by stamping the stamp twice
                if mark[i][j+1] == '#' and mark[i+1][j] == '#':
                    return num_hashes // 2
    
    # If the mark cannot be formed by stamping the stamp twice, return -1
    return -1

def f2(n, m, mark):
    # Initialize a dictionary to store the number of '#' in each row and column
    row_counts = {}
    col_counts = {}
    
    # Loop through the mark and count the number of '#' in each row and column
    for i in range(n):
        for j in range(m):
            if mark[i][j] == '#':
                if i not in row_counts:
                    row_counts[i] = 1
                else:
                    row_counts[i] += 1
                if j not in col_counts:
                    col_counts[j] = 1
                else:
                    col_counts[j] += 1
    
    # Initialize a set to store the possible number of '#' in the stamp
    possible_num_hashes = set()
    
    # Loop through the row and column counts and check if they are even
    for i in row_counts:
        if row_counts[i] % 2 == 0:
            possible_num_hashes.add(row_counts[i] // 2)
    for j in col_counts:
        if col_counts[j] % 2 == 0:
            possible_num_hashes.add(col_counts[j] // 2)
    
    # If the set of possible number of '#' is empty, return -1
    if not possible_num_hashes:
        return -1
    
    # Return the minimum number of '#' in the stamp
    return min(possible_num_hashes)

if __name__ == '__main__':
    n, m, mark = read_input()
    print(f1(n, m, mark))
    print(f2(n, m, mark))

