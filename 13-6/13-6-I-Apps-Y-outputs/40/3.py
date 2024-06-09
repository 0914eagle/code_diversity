
def get_divisible_elements(arr):
    # Your code here
    return ...

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(get_divisible_elements(arr))

if __name__ == '__main__':
    main()

