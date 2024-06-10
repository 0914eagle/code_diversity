
def get_distinct_sizes(sizes):
    return len(set(sizes))

def get_max_diff(sizes):
    return max(sizes) - min(sizes)

def can_give_gifts(sizes):
    distinct_sizes = get_distinct_sizes(sizes)
    max_diff = get_max_diff(sizes)
    return distinct_sizes == 3 and max_diff <= 2

def main():
    n = int(input())
    sizes = list(map(int, input().split()))
    if can_give_gifts(sizes):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

