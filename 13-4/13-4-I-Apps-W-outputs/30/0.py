
def is_connected(house_num, connected_houses):
    for house in connected_houses:
        if house_num in house:
            return True
    return False

def get_not_connected_houses(connected_houses):
    not_connected_houses = []
    for house_num in range(1, len(connected_houses) + 1):
        if not is_connected(house_num, connected_houses):
            not_connected_houses.append(house_num)
    return not_connected_houses

def main():
    num_houses, num_cables = map(int, input().split())
    connected_houses = []
    for _ in range(num_cables):
        house1, house2 = map(int, input().split())
        connected_houses.append((house1, house2))
    not_connected_houses = get_not_connected_houses(connected_houses)
    if not not_connected_houses:
        print("Connected")
    else:
        for house_num in not_connected_houses:
            print(house_num)

if __name__ == '__main__':
    main()

