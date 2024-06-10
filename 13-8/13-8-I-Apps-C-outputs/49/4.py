
def get_input():
    n = int(input())
    sizes = list(map(int, input().split()))
    return n, sizes

def is_valid_choice(sizes):
    sizes.sort()
    for i in range(len(sizes) - 2):
        if sizes[i] + 2 < sizes[i + 2]:
            return False
    return True

def main():
    n, sizes = get_input()
    if len(sizes) < 3:
        print("NO")
    elif is_valid_choice(sizes):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

