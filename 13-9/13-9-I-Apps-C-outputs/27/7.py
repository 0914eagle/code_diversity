
def get_total_chairs(n, guests):
    total_chairs = 0
    for guest in guests:
        total_chairs += guest[0] + guest[1] + 1
    return total_chairs

def get_guests_with_overlapping_chairs(n, guests):
    guests_with_overlapping_chairs = []
    for i in range(n):
        for j in range(i+1, n):
            if guests[i][0] + guests[i][1] + 1 >= guests[j][0] + guests[j][1] + 1:
                guests_with_overlapping_chairs.append(i)
                break
    return guests_with_overlapping_chairs

def get_optimal_number_of_chairs(n, guests):
    total_chairs = get_total_chairs(n, guests)
    guests_with_overlapping_chairs = get_guests_with_overlapping_chairs(n, guests)
    if len(guests_with_overlapping_chairs) == 0:
        return total_chairs
    else:
        return total_chairs + len(guests_with_overlapping_chairs)

def main():
    n = int(input())
    guests = []
    for i in range(n):
        l, r = map(int, input().split())
        guests.append((l, r))
    print(get_optimal_number_of_chairs(n, guests))

if __name__ == '__main__':
    main()

