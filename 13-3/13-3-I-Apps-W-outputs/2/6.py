
def get_car_sizes(father_size, mother_size, son_size, masha_size):
    # Check if the given sizes satisfy the conditions
    if father_size > mother_size > son_size and masha_size > son_size:
        # Find the possible sizes of the cars
        father_car_size = father_size
        mother_car_size = mother_size - 1
        son_car_size = son_size - 1
        return father_car_size, mother_car_size, son_car_size
    else:
        return -1

if __name__ == '__main__':
    father_size = int(input())
    mother_size = int(input())
    son_size = int(input())
    masha_size = int(input())
    car_sizes = get_car_sizes(father_size, mother_size, son_size, masha_size)
    if car_sizes == -1:
        print(-1)
    else:
        print(car_sizes[0])
        print(car_sizes[1])
        print(car_sizes[2])

