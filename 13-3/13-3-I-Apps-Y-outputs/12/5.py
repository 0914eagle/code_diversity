
def get_min_lcm(arr):
    # Sort the array in ascending order
    arr.sort()
    # Initialize the minimum LCM and its indices
    min_lcm = 0
    i, j = 0, 0
    # Iterate through the array
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            # Calculate the LCM of the current pair
            lcm = arr[i] * arr[j] // gcd(arr[i], arr[j])
            # If the LCM is less than the minimum LCM, update the minimum LCM and its indices
            if lcm < min_lcm or min_lcm == 0:
                min_lcm = lcm
                i_min, j_min = i, j
    return i_min + 1, j_min + 1

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    arr = [int(input()) for _ in range(int(input()))]
    print(*get_min_lcm(arr))

