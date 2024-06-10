
def is_perfect_square(n):
    return int(n**0.5)**2 == n

def find_largest_non_perfect_square(arr):
    largest = 0
    for i in range(len(arr)):
        if not is_perfect_square(arr[i]) and arr[i] > largest:
            largest = arr[i]
    return largest

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(find_largest_non_perfect_square(arr))

if __name__ == '__main__':
    main()

