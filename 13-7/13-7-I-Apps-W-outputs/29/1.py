
def get_min_sweets(n, t, street):
    # Initialize variables
    k = 0
    time = 0
    houses = 0
    shops = 0
    visited_shops = set()

    # Iterate through the street
    for i in range(n):
        if street[i] == "H":
            houses += 1
        elif street[i] == "S":
            shops += 1

    # Iterate through the street again
    for i in range(n):
        if street[i] == "H":
            k += 1
            time += 1
            houses -= 1
        elif street[i] == "S":
            if len(visited_shops) < shops:
                k += 1
                time += 1
                visited_shops.add(i)
            else:
                time += 1
        else:
            time += 1

        if time > t:
            return -1

    return k

def main():
    n, t = map(int, input().split())
    street = input()
    print(get_min_sweets(n, t, street))

if __name__ == '__main__':
    main()

