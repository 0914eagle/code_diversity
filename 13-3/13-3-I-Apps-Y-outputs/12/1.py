
def get_lcm(a, b):
    # Calculate the greatest common divisor of a and b
    gcd = _get_gcd(a, b)
    # Return the least common multiple as the product of a and b divided by their gcd
    return a * b // gcd

def _get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def get_min_lcm_pair(arr):
    # Initialize the minimum lcm value to a large number
    min_lcm = float('inf')
    # Initialize the indices of the minimum lcm pair to -1
    min_lcm_pair = [-1, -1]
    # Iterate over the pairs of indices in the array
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            # Calculate the lcm of the current pair of indices
            lcm = get_lcm(arr[i], arr[j])
            # If the lcm is less than the minimum lcm, update the minimum lcm and the minimum lcm pair
            if lcm < min_lcm:
                min_lcm = lcm
                min_lcm_pair = [i, j]
    # Return the minimum lcm pair
    return min_lcm_pair

if __name__ == '__main__':
    arr = [int(input()) for _ in range(int(input()))]
    print(*get_min_lcm_pair(arr))

