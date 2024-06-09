
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

def main():
    father_size, mother_size, son_size, masha_size = map(int, input().split())
    print(*get_car_sizes(father_size, mother_size, son_size, masha_size))

if __name__ == '__main__':
    main()

