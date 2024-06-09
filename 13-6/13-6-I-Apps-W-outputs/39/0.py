
def get_car_sizes(father_size, mother_size, son_size, masha_size):
    # Initialize possible car sizes
    car_sizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Create a list of possible combinations of car sizes
    combinations = []
    for i in range(len(car_sizes)):
        for j in range(i+1, len(car_sizes)):
            for k in range(j+1, len(car_sizes)):
                combinations.append([car_sizes[i], car_sizes[j], car_sizes[k]])
    
    # Iterate through the combinations and check if they satisfy the conditions
    for combination in combinations:
        # Check if Masha can climb into the smallest car
        if combination[2] >= masha_size:
            # Check if the father can climb into the largest car and like it
            if combination[0] >= father_size and 2*father_size >= combination[0]:
                # Check if the mother can climb into the middle car and like it
                if combination[1] >= mother_size and 2*mother_size >= combination[1]:
                    # Check if the son can climb into the smallest car and like it
                    if combination[2] >= son_size and 2*son_size >= combination[2]:
                        return combination
    
    # If no combination is found, return -1
    return -1

def main():
    father_size, mother_size, son_size, masha_size = map(int, input().split())
    print(get_car_sizes(father_size, mother_size, son_size, masha_size))

if __name__ == '__main__':
    main()

