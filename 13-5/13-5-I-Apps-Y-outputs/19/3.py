
def get_input():
    return list(map(int, input().split()))

def is_ac(n, m):
    return m == n

def main():
    n, m = get_input()
    if is_ac(n, m):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

