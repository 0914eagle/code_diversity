
def arrange_guests(n, guests):
    guests.sort(key=lambda x: x[0] + x[1], reverse=True)
    
    total_chairs = 0
    max_free_chairs = 0
    
    for guest in guests:
        total_chairs += max(guest[0] + guest[1] - max_free_chairs, 0)
        max_free_chairs = max(max_free_chairs, guest[0])
    
    return total_chairs

if __name__ == '__main__':
    n = int(input())
    guests = [list(map(int, input().split())) for _ in range(n)]
    
    result = arrange_guests(n, guests)
    print(result)
