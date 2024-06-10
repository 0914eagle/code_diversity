
def get_good_times(hours, l, r, a_list):
    good_times = 0
    current_time = 0
    for a in a_list:
        if l <= current_time <= r:
            good_times += 1
        current_time += a
    return good_times

def main():
    n, h, l, r = map(int, input().split())
    a_list = list(map(int, input().split()))
    print(get_good_times(h, l, r, a_list))

if __name__ == '__main__':
    main()

