
def get_distinct_sizes(ball_sizes):
    return len(set(ball_sizes)) == 3

def get_sizes_diff_less_than_or_equal_to_2(ball_sizes):
    return all(abs(ball_sizes[i] - ball_sizes[i+1]) <= 2 for i in range(len(ball_sizes)-1))

def can_give_gifts(n, ball_sizes):
    if n != 3:
        return False
    if not get_distinct_sizes(ball_sizes):
        return False
    if not get_sizes_diff_less_than_or_equal_to_2(ball_sizes):
        return False
    return True

if __name__ == '__main__':
    n = int(input())
    ball_sizes = [int(size) for size in input().split()]
    print("YES") if can_give_gifts(n, ball_sizes) else print("NO")

