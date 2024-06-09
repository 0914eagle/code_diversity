
def is_ac(n, m):
    return "Yes" if m == n else "No"

def main():
    n, m = map(int, input().split())
    print(is_ac(n, m))

if __name__ == '__main__':
    main()

