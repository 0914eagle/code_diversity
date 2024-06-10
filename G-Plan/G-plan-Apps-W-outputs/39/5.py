
from math import gcd

def smallest_subset_with_gcd_one(n, sequence):
    current_gcd = sequence[0]
    for i in range(1, n):
        current_gcd = gcd(current_gcd, sequence[i])
        if current_gcd == 1:
            return i + 1
    return -1

if __name__ == "__main__":
    n = int(input())
    sequence = list(map(int, input().split()))
    result = smallest_subset_with_gcd_one(n, sequence)
    print(result)
