
def get_car_sizes(father_bear_size, mother_bear_size, son_bear_size, masha_size):
    # Check if the conditions for the sizes of the bears and Masha are satisfied
    if father_bear_size > mother_bear_size > son_bear_size and masha_size > son_bear_size:
        # Find the possible sizes of the cars
        father_car_size = father_bear_size
        mother_car_size = mother_bear_size
        son_car_size = son_bear_size
        return father_car_size, mother_car_size, son_car_size
    else:
        return -1

def main():
    father_bear_size, mother_bear_size, son_bear_size, masha_size = map(int, input().split())
    car_sizes = get_car_sizes(father_bear_size, mother_bear_size, son_bear_size, masha_size)
    if car_sizes != -1:
        print(car_sizes[0], car_sizes[1], car_sizes[2])
    else:
        print(-1)

if __name__ == '__main__':
    main()

