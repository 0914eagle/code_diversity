
def is_connected(house_num, connected_houses):
    for connected_house in connected_houses:
        if house_num == connected_house or house_num in connected_houses[connected_house]:
            return True
    return False

def get_not_connected_houses(n, m, connected_houses):
    not_connected_houses = []
    for i in range(1, n+1):
        if not is_connected(i, connected_houses):
            not_connected_houses.append(i)
    return not_connected_houses

def main():
    n, m = map(int, input().split())
    connected_houses = {}
    for _ in range(m):
        house1, house2 = map(int, input().split())
        if house1 not in connected_houses:
            connected_houses[house1] = [house2]
        else:
            connected_houses[house1].append(house2)
        if house2 not in connected_houses:
            connected_houses[house2] = [house1]
        else:
            connected_houses[house2].append(house1)
    not_connected_houses = get_not_connected_houses(n, m, connected_houses)
    if len(not_connected_houses) == 0:
        print("Connected")
    else:
        for house in not_connected_houses:
            print(house)

if __name__ == '__main__':
    main()

