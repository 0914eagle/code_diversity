
def is_interval_exists(a, b):
    # Write your code here
    return "YES" if a + b <= 100 else "NO"

def main():
    a, b = map(int, input().split())
    print(is_interval_exists(a, b))

if __name__ == '__main__':
    main()

