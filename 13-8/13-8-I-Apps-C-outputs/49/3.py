
def get_distinct_sizes(t_list):
    return len(set(t_list))

def get_max_difference(t_list):
    return max(t_list) - min(t_list)

def can_choose_three_balls(t_list):
    if get_distinct_sizes(t_list) < 3:
        return False
    if get_max_difference(t_list) > 2:
        return False
    return True

def main():
    n = int(input())
    t_list = list(map(int, input().split()))
    if can_choose_three_balls(t_list):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

