
import sys

def get_possible_sums(N, K):
    # Calculate the possible sums
    possible_sums = []
    for i in range(N+1):
        for j in range(i+1, N+1):
            possible_sums.append(i+j)
    
    # Return the number of possible sums
    return len(set(possible_sums))

if __name__ == '__main__':
    N, K = map(int, input().split())
    print(get_possible_sums(N, K))

