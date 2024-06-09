
def find_min_lcm(arr):
    # Find the least common multiple of the first two elements
    lcm = arr[0] * arr[1] // gcd(arr[0], arr[1])
    
    # Iterate through the rest of the elements
    for i in range(2, len(arr)):
        # Find the least common multiple of the current element and the previous lcm
        lcm = lcm * arr[i] // gcd(lcm, arr[i])
    
    return lcm

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    arr = [int(input()) for _ in range(int(input()))]
    print(find_min_lcm(arr))

