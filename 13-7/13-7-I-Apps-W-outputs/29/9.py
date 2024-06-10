
def get_min_sweets(n, t, street):
    # Initialize variables
    k = 0
    time = 0
    houses = 0
    shops = 0
    visited = [False] * n
    shop_visited = [False] * n

    # Loop through the street
    for i in range(n):
        # If the current segment is a house, increment the number of houses
        if street[i] == "H":
            houses += 1
        # If the current segment is a shop, increment the number of shops
        elif street[i] == "S":
            shops += 1
        # If the current segment is empty, skip it
        else:
            continue

        # If the current segment has not been visited and there are still sweets left, visit it
        if not visited[i] and k > 0:
            visited[i] = True
            k -= 1
            time += 1

        # If the current segment is a shop and it has not been visited, visit it
        if shop_visited[i] == False and shops > 0:
            shop_visited[i] = True
            shops -= 1
            time += 1

        # If the current segment is a house and it has not been visited, visit it
        if visited[i] == False and houses > 0:
            visited[i] = True
            houses -= 1
            time += 1

    # If there are still sweets left and there are still houses to visit, give one kilogram of sweets to each house
    while k > 0 and houses > 0:
        k -= 1
        houses -= 1
        time += 1

    # If there are still sweets left and there are still shops to visit, buy one kilogram of sweets from each shop
    while k > 0 and shops > 0:
        k -= 1
        shops -= 1
        time += 1

    # Return the minimum number of kilograms of sweets needed to give sweets to all the houses in at most t units of time
    return k

def main():
    n, t = map(int, input().split())
    street = list(input())
    print(get_min_sweets(n, t, street))

if __name__ == '__main__':
    main()

