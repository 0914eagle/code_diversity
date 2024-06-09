
def get_car_sizes(father_bear_size, mother_bear_size, son_bear_size, masha_size):
    # Check if the given sizes satisfy the conditions
    if father_bear_size > mother_bear_size > son_bear_size and masha_size > son_bear_size:
        # Find the possible sizes of the cars
        father_car_size = father_bear_size
        mother_car_size = mother_bear_size
        son_car_size = son_bear_size
        return father_car_size, mother_car_size, son_car_size
    else:
        return -1

if __name__ == '__main__':
    father_bear_size = int(input())
    mother_bear_size = int(input())
    son_bear_size = int(input())
    masha_size = int(input())
    print(get_car_sizes(father_bear_size, mother_bear_size, son_bear_size, masha_size))

