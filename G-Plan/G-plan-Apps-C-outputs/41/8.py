
def arrange_guests():
    n = int(input())
    guests = []
    for _ in range(n):
        l, r = map(int, input().split())
        guests.append((l, r))

    guests.sort(key=lambda x: x[0] + x[1], reverse=True)

    total_chairs = 0
    max_free_chairs = 0
    for l, r in guests:
        total_chairs += max(l + r - max_free_chairs, 0)
        max_free_chairs = max(max_free_chairs, l)

    print(total_chairs)

if __name__ == '__main__':
    arrange_guests()
