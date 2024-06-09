
def is_ac(n, m):
    if m == n:
        return "Yes"
    else:
        return "No"

def main():
    n, m = map(int, input().split())
    print(is_ac(n, m))

if __name__ == '__main__':
    main()

