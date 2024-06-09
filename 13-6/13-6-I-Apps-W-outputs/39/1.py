
def get_car_sizes(father_size, mother_size, son_size, masha_size):
    # Initialize variables
    father_car_size = 0
    mother_car_size = 0
    son_car_size = 0

    # Check if Masha can climb into the smallest car
    if masha_size <= son_size:
        # Masha can climb into the smallest car, so son bear likes it
        son_car_size = son_size

        # Check if father bear can climb into the middle car
        if father_size <= mother_size:
            # Father bear can climb into the middle car, so mother bear likes it
            mother_car_size = mother_size

            # Check if the middle car is larger than the smallest car
            if mother_car_size > son_car_size:
                # The middle car is larger than the smallest car, so father bear likes it
                father_car_size = father_size
    else:
        # Masha cannot climb into the smallest car, so there is no solution
        father_car_size = -1

    return father_car_size, mother_car_size, son_car_size

def main():
    father_size, mother_size, son_size, masha_size = map(int, input().split())
    father_car_size, mother_car_size, son_car_size = get_car_sizes(father_size, mother_size, son_size, masha_size)
    print(father_car_size, mother_car_size, son_car_size)

if __name__ == '__main__':
    main()

