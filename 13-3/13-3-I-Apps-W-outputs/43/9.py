
def get_good_matrix(a):
    # Initialize variables
    n, m = len(a), len(a[0])
    count = 0
    
    # Loop through each sub-matrix
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    # Check if sub-matrix is even length square
                    if k-i+1 == l-j+1 and (k-i+1) % 2 == 0:
                        # Count the number of ones in the sub-matrix
                        ones = 0
                        for r in range(i, k+1):
                            for c in range(j, l+1):
                                if a[r][c] == 1:
                                    ones += 1
                        # If the number of ones is odd, we cannot make the sub-matrix good
                        if ones % 2 == 1:
                            return -1
    
    # If we reach this point, we can make the matrix good by changing at most count cells
    return count

def main():
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input())))
    print(get_good_matrix(a))

if __name__ == '__main__':
    main()

