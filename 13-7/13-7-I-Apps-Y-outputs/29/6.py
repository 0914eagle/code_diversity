
def is_similar(x, y):
    return x % 2 == y % 2 or abs(x - y) == 1

def can_partition_into_similar_pairs(arr):
    n = len(arr)
    if n % 2 == 1:
        return False
    for i in range(0, n, 2):
        x = arr[i]
        y = arr[i + 1]
        if not is_similar(x, y):
            return False
    return True

def main():
    num_test_cases = int(input())
    for i in range(num_test_cases):
        n = int(input())
        arr = list(map(int, input().split()))
        if can_partition_into_similar_pairs(arr):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()

