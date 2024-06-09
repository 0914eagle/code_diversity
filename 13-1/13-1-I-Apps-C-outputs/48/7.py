
n = int(input())
a = list(map(int, input().split()))

def get_min_hours(k):
    hours = 0
    while len([x for x in a if x > 0]) < k:
        hours += 1
        a = [x - 1 if x > 0 else 0 for x in a]
    return hours

print(*[get_min_hours(i) for i in range(1, int(n/2)+1)], sep=' ')

