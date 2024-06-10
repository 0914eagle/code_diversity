
def find_floor(n, m, polycarp_memory):
    # Initialize a dictionary to store the number of flats on each floor
    num_flats_on_each_floor = {}

    # Iterate over the Polycarp's memory
    for flat, floor in polycarp_memory:
        # If the floor is not in the dictionary, add it with a value of 1
        if floor not in num_flats_on_each_floor:
            num_flats_on_each_floor[floor] = 1
        # If the floor is already in the dictionary, increment its value by 1
        else:
            num_flats_on_each_floor[floor] += 1

    # Initialize a variable to store the number of flats on each floor
    num_flats_on_each_floor_list = []

    # Iterate over the dictionary and append the number of flats on each floor to the list
    for floor, num_flats in num_flats_on_each_floor.items():
        num_flats_on_each_floor_list.append(num_flats)

    # Sort the list in descending order
    num_flats_on_each_floor_list.sort(reverse=True)

    # Initialize a variable to store the index of the floor with the highest number of flats
    max_index = 0

    # Iterate over the list and find the index of the floor with the highest number of flats
    for i in range(len(num_flats_on_each_floor_list)):
        if num_flats_on_each_floor_list[i] == num_flats_on_each_floor_list[max_index]:
            max_index = i

    # Return the floor number if it is possible to uniquely restore it, otherwise return -1
    if num_flats_on_each_floor_list[max_index] * (max_index + 1) >= n:
        return max_index + 1
    else:
        return -1

def main():
    n, m = map(int, input().split())
    polycarp_memory = []
    for _ in range(m):
        flat, floor = map(int, input().split())
        polycarp_memory.append((flat, floor))
    print(find_floor(n, m, polycarp_memory))

if __name__ == '__main__':
    main()

