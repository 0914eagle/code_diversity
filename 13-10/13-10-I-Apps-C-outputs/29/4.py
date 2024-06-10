
import math

def get_input():
    n, s, t, q = map(int, input().split())
    hills = []
    for _ in range(n):
        x, y, h = map(int, input().split())
        hills.append((x, y, h))
    springs = set(map(int, input().split()))
    towns = set(map(int, input().split()))
    return n, s, t, q, hills, springs, towns

def possible(hill, springs, towns, q):
    if hill[2] in springs and hill[2] in towns:
        return False
    if hill[2] in springs:
        return True
    if hill[2] in towns:
        return True
    for i in range(len(hills)):
        if hills[i][2] == hill[2] and abs(hills[i][1] - hill[1]) <= q and abs(hills[i][0] - hill[0]) <= q:
            return True
    return False

def solve(n, s, t, q, hills, springs, towns):
    total_length = 0
    for i in range(n):
        if possible(hills[i], springs, towns, q):
            total_length += math.sqrt((hills[i][0] - hills[i-1][0])**2 + (hills[i][1] - hills[i-1][1])**2)
    return total_length

def main():
    n, s, t, q, hills, springs, towns = get_input()
    print(solve(n, s, t, q, hills, springs, towns))

if __name__ == '__main__':
    main()

