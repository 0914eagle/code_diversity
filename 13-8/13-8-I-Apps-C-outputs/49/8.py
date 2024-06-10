
def get_distinct_sizes(sizes):
    return len(set(sizes)) == 3

def get_difference_less_than_or_equal_to_2(sizes):
    return all(abs(sizes[i] - sizes[i+1]) <= 2 for i in range(len(sizes)-1))

def can_choose_three_balls(n, sizes):
    return get_distinct_sizes(sizes) and get_difference_less_than_or_equal_to_2(sizes)

def main():
    n = int(input())
    sizes = list(map(int, input().split()))
    print("YES") if can_choose_three_balls(n, sizes) else print("NO")

if __name__ == '__main__':
    main()

