
def f1(k):
    # find the maximum live duration of all allergens
    max_duration = max(map(int, input().split()))

    # calculate the number of days needed for the shortest conclusive non-adaptive test scheme
    num_days = max_duration * k

    return num_days

def f2(k):
    # find the maximum live duration of all allergens
    max_duration = max(map(int, input().split()))

    # calculate the number of days needed for the shortest conclusive non-adaptive test scheme
    num_days = max_duration * k

    return num_days

if __name__ == '__main__':
    k = int(input())
    print(f1(k))
    print(f2(k))

