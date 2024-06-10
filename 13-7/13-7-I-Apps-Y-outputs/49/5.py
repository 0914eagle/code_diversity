
def check_condition(a, b, c):
    if a <= c <= b:
        return "Yes"
    else:
        return "No"

def main():
    a, b, c = map(int, input().split())
    print(check_condition(a, b, c))

if __name__ == '__main__':
    main()

