
def get_input():
    return list(map(int, input().split()))

def check_ac(n, m):
    return "Yes" if m == n else "No"

def main():
    n, m = get_input()
    print(check_ac(n, m))

if __name__ == '__main__':
    main()

