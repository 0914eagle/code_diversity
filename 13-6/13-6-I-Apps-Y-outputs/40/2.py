
def get_max_divisible_by_3(a):
    # Your code here
    return max_divisible_by_3

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(get_max_divisible_by_3(a))

if __name__ == '__main__':
    main()

