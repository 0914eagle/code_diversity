
def get_car_sizes(father_size, mother_size, son_size, masha_size):
    # Initialize the possible car sizes
    car_sizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Create a dictionary to store the possible car sizes for each bear
    bear_car_sizes = {
        "father": [],
        "mother": [],
        "son": [],
        "masha": []
    }
    
    # Loop through the possible car sizes and check if they satisfy the conditions for each bear
    for car_size in car_sizes:
        # Father bear can climb into the largest car
        if car_size >= father_size:
            bear_car_sizes["father"].append(car_size)
        # Mother bear can climb into the middle car
        if car_size >= mother_size:
            bear_car_sizes["mother"].append(car_size)
        # Son bear can climb into the smallest car
        if car_size >= son_size:
            bear_car_sizes["son"].append(car_size)
        # Masha can climb into the smallest car
        if car_size >= masha_size:
            bear_car_sizes["masha"].append(car_size)
    
    # Check if there is a possible solution
    if len(bear_car_sizes["father"]) == 0 or len(bear_car_sizes["mother"]) == 0 or len(bear_car_sizes["son"]) == 0 or len(bear_car_sizes["masha"]) == 0:
        return [-1, -1, -1]
    
    # Find the intersection of the possible car sizes for each bear
    intersection = set(bear_car_sizes["father"]).intersection(set(bear_car_sizes["mother"]))
    intersection = set(intersection).intersection(set(bear_car_sizes["son"]))
    intersection = set(intersection).intersection(set(bear_car_sizes["masha"]))
    
    # If there is no intersection, return -1
    if len(intersection) == 0:
        return [-1, -1, -1]
    
    # Return the first element of the intersection as the solution
    return [intersection.pop(), intersection.pop(), intersection.pop()]

def main():
    father_size, mother_size, son_size, masha_size = map(int, input().split())
    print(get_car_sizes(father_size, mother_size, son_size, masha_size))

if __name__ == '__main__':
    main()

