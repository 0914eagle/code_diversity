
def arrange_guests():
    n = int(input())
    guests = []
    for _ in range(n):
        l, r = map(int, input().split())
        guests.append((l, r, l + r))
    
    guests.sort(key=lambda x: x[2], reverse=True)
    
    total_chairs = 0
    max_free_chairs = 0
    for guest in guests:
        total_chairs += max(max_free_chairs, guest[2]) + 1
        max_free_chairs = max(max_free_chairs, guest[2])
    
    print(total_chairs)

if __name__ == '__main__':
    arrange_guests()
