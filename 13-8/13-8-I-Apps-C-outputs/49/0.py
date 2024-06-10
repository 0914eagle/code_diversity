
def input_data():
    n = int(input())
    sizes = list(map(int, input().split()))
    return n, sizes

def find_distinct_sizes(sizes):
    return len(set(sizes)) == 3

def find_difference_less_than_or_equal_to_2(sizes):
    for i in range(len(sizes) - 1):
        for j in range(i + 1, len(sizes)):
            if abs(sizes[i] - sizes[j]) > 2:
                return False
    return True

def main():
    n, sizes = input_data()
    if find_distinct_sizes(sizes) and find_difference_less_than_or_equal_to_2(sizes):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

