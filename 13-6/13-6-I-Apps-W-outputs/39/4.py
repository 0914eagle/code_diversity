
def get_car_sizes(father_size, mother_size, son_size, masha_size):
    # Check if Masha can climb into the smallest car
    if masha_size > son_size:
        return -1
    
    # Check if son bear can like the smallest car
    if son_size * 2 < masha_size:
        return -1
    
    # Check if father bear can climb into the largest car
    if father_size < masha_size:
        return -1
    
    # Check if mother bear can climb into the middle car
    if mother_size < masha_size:
        return -1
    
    # Return the possible sizes of the cars
    return father_size, mother_size, son_size

def main():
    father_size, mother_size, son_size, masha_size = map(int, input().split())
    print(*get_car_sizes(father_size, mother_size, son_size, masha_size))

if __name__ == '__main__':
    main()

