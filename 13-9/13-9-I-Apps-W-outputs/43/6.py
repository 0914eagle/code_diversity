
def is_divisible(numbers, m):
    # implement your solution here
    return True

def main():
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    result = "YES" if is_divisible(numbers, m) else "NO"
    print(result)

if __name__ == '__main__':
    main()

