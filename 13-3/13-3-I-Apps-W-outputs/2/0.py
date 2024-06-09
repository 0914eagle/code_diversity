
def get_car_sizes(father_size, mother_size, son_size, masha_size):
    # Initialize variables
    father_car_size = 0
    mother_car_size = 0
    son_car_size = 0

    # Check if the conditions for the cars' sizes are satisfied
    if father_size > mother_size and mother_size > son_size and masha_size > son_size:
        # Find the possible sizes of the cars
        father_car_size = father_size
        mother_car_size = mother_size - 1
        son_car_size = son_size - 1

        # Check if Masha can climb into the smallest car and likes it
        if son_car_size >= masha_size and 2 * son_car_size >= masha_size:
            return father_car_size, mother_car_size, son_car_size

    # If no solution is found, return -1
    return -1, -1, -1

if __name__ == '__main__':
    father_size = 50
    mother_size = 30
    son_size = 10
    masha_size = 10
    print(get_car_sizes(father_size, mother_size, son_size, masha_size))

