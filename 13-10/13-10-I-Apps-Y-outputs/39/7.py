
def partition_exists(a):
    # Sort the array
    a.sort()
    # Initialize two pointers for the start and end of the array
    start, end = 0, len(a) - 1
    # Iterate through the array
    while start < end:
        # If the two elements are similar, move both pointers up by 1
        if a[start] + 1 == a[end] or a[start] == a[end] // 2:
            start += 1
            end -= 1
        # If the two elements are not similar, return False
        else:
            return False
    # If we reach the end of the array, return True
    return True

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print("YES") if partition_exists(a) else print("NO")

if __name__ == '__main__':
    main()

