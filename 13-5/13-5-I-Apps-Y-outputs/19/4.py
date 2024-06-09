
def get_input():
    return input().split()

def is_ac(n, m):
    return m == n

def main():
    n, m = get_input()
    if is_ac(int(n), int(m)):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

