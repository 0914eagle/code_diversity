
def remove_duplicates(a):
    seen = set()
    unique = []
    for x in a:
        if x not in seen:
            unique.append(x)
            seen.add(x)
    return unique

def get_rightmost_unique_elements(a):
    unique = remove_duplicates(a)
    rightmost = []
    for x in unique:
        rightmost.append(x)
    return rightmost

def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = len(get_rightmost_unique_elements(a))
    print(x)
    print(" ".join(map(str, get_rightmost_unique_elements(a))))

if __name__ == '__main__':
    main()

