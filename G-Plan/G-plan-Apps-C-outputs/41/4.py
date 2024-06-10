
def arrange_guests():
    n = int(input())
    guests = []
    for _ in range(n):
        l, r = map(int, input().split())
        guests.append((l, r))

    guests.sort(key=lambda x: x[0] + x[1], reverse=True)

    total_chairs = 0
    max_free_chairs = 0
    for guest in guests:
        total_chairs += max(max_free_chairs + guest[0] + guest[1], total_chairs)
        max_free_chairs = max(max_free_chairs, guest[0])

    print(total_chairs)

if __name__ == '__main__':
    arrange_guests()
