
def get_car_sizes(father_size, mother_size, son_size, masha_size):
    # Check if Masha can climb into the smallest car
    if masha_size <= son_size:
        # Check if son bear likes the smallest car
        if 2 * son_size >= son_size:
            # Check if father bear can climb into the middle car
            if father_size <= mother_size:
                # Check if mother bear likes the middle car
                if 2 * mother_size >= mother_size:
                    # Check if son bear can climb into the largest car
                    if son_size <= father_size:
                        # Check if father bear likes the largest car
                        if 2 * father_size >= father_size:
                            return father_size, mother_size, son_size
    return -1

def main():
    father_size, mother_size, son_size, masha_size = map(int, input().split())
    print(get_car_sizes(father_size, mother_size, son_size, masha_size))

if __name__ == '__main__':
    main()

