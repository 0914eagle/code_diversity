
def get_distinct_sizes(sizes):
    return len(set(sizes))

def get_sizes_difference(sizes):
    return max(sizes) - min(sizes)

def can_choose_three_balls(n, sizes):
    if get_distinct_sizes(sizes) < 3:
        return False
    if get_sizes_difference(sizes) > 2:
        return False
    return True

def main():
    n = int(input())
    sizes = list(map(int, input().split()))
    if can_choose_three_balls(n, sizes):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

