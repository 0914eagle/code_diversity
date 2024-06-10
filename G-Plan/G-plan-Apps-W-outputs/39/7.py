
from math import gcd

def find_smallest_subset_with_gcd_one(n, arr):
    current_gcd = arr[0]
    if current_gcd != 1:
        return -1
    
    for i in range(1, n):
        current_gcd = gcd(current_gcd, arr[i])
        if current_gcd == 1:
            return i + 1
    
    return -1

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    
    result = find_smallest_subset_with_gcd_one(n, arr)
    print(result)
