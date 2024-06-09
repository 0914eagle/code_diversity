
def get_car_sizes(father_bear_size, mother_bear_size, son_bear_size, masha_size):
    # Check if the given sizes satisfy the conditions
    if father_bear_size <= mother_bear_size and mother_bear_size <= son_bear_size and masha_size <= son_bear_size:
        # Find the possible sizes of the cars
        father_car_size = father_bear_size
        mother_car_size = mother_bear_size
        son_car_size = son_bear_size
        while father_car_size >= son_car_size:
            if 2 * father_car_size >= son_car_size:
                break
            father_car_size -= 1
        while mother_car_size >= son_car_size:
            if 2 * mother_car_size >= son_car_size:
                break
            mother_car_size -= 1
        while son_car_size >= masha_size:
            if 2 * son_car_size >= masha_size:
                break
            son_car_size -= 1
        # Return the possible sizes of the cars
        return father_car_size, mother_car_size, son_car_size
    else:
        # If the given sizes do not satisfy the conditions, return -1
        return -1

def main():
    father_bear_size, mother_bear_size, son_bear_size, masha_size = map(int, input().split())
    car_sizes = get_car_sizes(father_bear_size, mother_bear_size, son_bear_size, masha_size)
    if car_sizes == -1:
        print(-1)
    else:
        print(*car_sizes)

if __name__ == '__main__':
    main()

