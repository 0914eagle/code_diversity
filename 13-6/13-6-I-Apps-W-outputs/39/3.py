
def get_car_sizes(father_size, mother_size, son_size, masha_size):
    # Check if Masha can climb into the smallest car
    if masha_size <= son_size:
        # If Masha can climb into the smallest car, then the smallest car size is 2 * son_size
        smallest_car_size = 2 * son_size
        # Check if the smallest car size is less than or equal to the father and mother car sizes
        if smallest_car_size <= father_size and smallest_car_size <= mother_size:
            # If the smallest car size is less than or equal to the father and mother car sizes, then the father and mother car sizes are the largest and middle car sizes, respectively
            largest_car_size = father_size
            middle_car_size = mother_size
            # The son car size is the smallest car size
            son_car_size = smallest_car_size
            return largest_car_size, middle_car_size, son_car_size
    # If Masha cannot climb into the smallest car, then there is no solution
    return -1

def main():
    father_size, mother_size, son_size, masha_size = map(int, input().split())
    largest_car_size, middle_car_size, son_car_size = get_car_sizes(father_size, mother_size, son_size, masha_size)
    if largest_car_size == -1:
        print(-1)
    else:
        print(largest_car_size, middle_car_size, son_car_size)

if __name__ == '__main__':
    main()

