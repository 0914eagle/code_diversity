
def check_condition(a, b, c):
    return a <= c and c <= b

def main():
    a, b, c = map(int, input().split())
    if check_condition(a, b, c):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

