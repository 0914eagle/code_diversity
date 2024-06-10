
def input_data():
    n = int(input())
    sizes = list(map(int, input().split()))
    return n, sizes

def check_sizes(sizes):
    sizes.sort()
    for i in range(len(sizes) - 2):
        if sizes[i + 1] - sizes[i] > 2:
            return False
    return True

def main():
    n, sizes = input_data()
    if len(sizes) < 3:
        print("NO")
    elif check_sizes(sizes):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

