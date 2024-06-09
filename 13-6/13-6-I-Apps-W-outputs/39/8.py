
def get_car_sizes(father_size, mother_size, son_size, masha_size):
    # Check if the conditions for the cars' sizes are satisfied
    if father_size > mother_size > son_size and masha_size <= son_size and 2 * son_size >= masha_size:
        return father_size, mother_size, son_size
    else:
        return -1

def main():
    father_size, mother_size, son_size, masha_size = map(int, input().split())
    print(get_car_sizes(father_size, mother_size, son_size, masha_size))

if __name__ == '__main__':
    main()

