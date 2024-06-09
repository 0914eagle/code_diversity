
def is_connected(house_num, connected_houses):
    for connected_house in connected_houses:
        if connected_house == house_num:
            return True
    return False

def get_not_connected_houses(connected_houses, total_houses):
    not_connected_houses = []
    for house_num in range(1, total_houses+1):
        if not is_connected(house_num, connected_houses):
            not_connected_houses.append(house_num)
    return not_connected_houses

def main():
    total_houses, total_cables = map(int, input().split())
    connected_houses = []
    for _ in range(total_cables):
        house1, house2 = map(int, input().split())
        connected_houses.append(house1)
        connected_houses.append(house2)
    not_connected_houses = get_not_connected_houses(connected_houses, total_houses)
    if len(not_connected_houses) == 0:
        print("Connected")
    else:
        for house_num in not_connected_houses:
            print(house_num)

if __name__ == '__main__':
    main()

