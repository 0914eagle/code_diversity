
def get_max_prettiness(a):
    # Sort the array in descending order
    a.sort(reverse=True)
    # Initialize the maximum prettiness as 0
    max_prettiness = 0
    # Loop through the array
    for i in range(len(a)):
        # Check if the current element is divisible by the previous elements
        for j in range(i-1, -1, -1):
            if a[i] % a[j] == 0:
                break
        else:
            # If the current element is not divisible by any of the previous elements, add it to the maximum prettiness
            max_prettiness += a[i]
    return max_prettiness

def main():
    q = int(input())
    for _ in range(q):
        n = int(input())
        a = list(map(int, input().split()))
        print(get_max_prettiness(a))

if __name__ == '__main__':
    main()

