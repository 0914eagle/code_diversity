
import sys
sys.setrecursionlimit(10**6)

def count_partitions(a, l, r):
    # Base case: if a is a single digit, return 1 if it is between l and r (inclusive), otherwise return 0
    if len(a) == 1:
        return 1 if int(a) in range(l, r+1) else 0
    
    # Initialize variables
    count = 0
    curr = ""
    
    # Recursive case: iterate through all possible partitions of a
    for i in range(1, len(a)):
        # Get the current partition and the remaining string
        curr, a = a[:i], a[i:]
        
        # If the current partition is between l and r (inclusive), recurse on the remaining string
        if int(curr) in range(l, r+1):
            count += count_partitions(a, l, r)
    
    return count

def main():
    a, l, r = map(int, input().split())
    print(count_partitions(str(a), l, r) % 998244353)

if __name__ == '__main__':
    main()

