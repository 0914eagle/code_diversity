
def get_max_divisible_by_3(arr):
    # Your code here
    return max_divisible_by_3

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(get_max_divisible_by_3(arr))

if __name__ == '__main__':
    main()

