
def find_min_lcm(arr):
    # Sort the array in ascending order
    arr.sort()
    # Initialize the minimum LCM and its indices
    min_lcm = 1
    min_indices = (0, 0)
    # Iterate through the array
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            # Calculate the LCM of the current pair
            lcm = arr[i] * arr[j] // gcd(arr[i], arr[j])
            # If the LCM is less than the minimum LCM, update the minimum LCM and its indices
            if lcm < min_lcm:
                min_lcm = lcm
                min_indices = (i, j)
    return min_indices

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(find_min_lcm(arr))

