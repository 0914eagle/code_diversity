
import sys

def solve(N, X, A):
    # Initialize the count of integers not exceeding X
    count = 0
    
    # Initialize the set of integers not exceeding X
    integers = set()
    
    # Add the initial integers to the set
    for i in range(N):
        integers.add(A[i])
    
    # Iterate through the integers in the set
    for i in integers:
        # If the integer is less than or equal to X, increment the count
        if i <= X:
            count += 1
        
        # If the integer is not already in the set, add its double and XOR to the set
        if i not in integers:
            integers.add(i * 2)
            integers.add(i ^ i)
    
    # Return the count modulo 998244353
    return count % 998244353

if __name__ == '__main__':
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    print(solve(N, X, A))

