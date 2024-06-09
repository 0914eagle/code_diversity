
def get_car_sizes(father_size, mother_size, son_size, masha_size):
    # Initialize variables
    father_car_size = 0
    mother_car_size = 0
    son_car_size = 0

    # Check if Masha can climb into the smallest car
    if masha_size <= son_size:
        # Masha can climb into the smallest car, so the smallest car size is 2 * son_size
        son_car_size = 2 * son_size

        # Check if father can climb into the middle car
        if father_size <= mother_size:
            # Father can climb into the middle car, so the middle car size is 2 * mother_size
            mother_car_size = 2 * mother_size

            # Check if mother can climb into the largest car
            if mother_size <= father_size:
                # Mother can climb into the largest car, so the largest car size is 2 * father_size
                father_car_size = 2 * father_size
            else:
                # Mother can't climb into the largest car, so there is no solution
                return -1
        else:
            # Father can't climb into the middle car, so there is no solution
            return -1
    else:
        # Masha can't climb into the smallest car, so there is no solution
        return -1

    # Return the car sizes
    return father_car_size, mother_car_size, son_car_size

if __name__ == '__main__':
    father_size = 50
    mother_size = 30
    son_size = 10
    masha_size = 10
    print(get_car_sizes(father_size, mother_size, son_size, masha_size))

