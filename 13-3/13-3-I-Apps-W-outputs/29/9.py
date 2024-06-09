
import sys

def get_possible_sums(n, k):
    # Calculate the possible sums
    possible_sums = []
    for i in range(n+1):
        for j in range(i+1, n+1):
            possible_sums.append(i+j)
    
    # Return the number of possible sums
    return len(set(possible_sums))

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(get_possible_sums(n, k))

