
import math

def get_hill_coordinates(n):
    return [(int(input()), int(input()), int(input())) for _ in range(n)]

def get_spring_hill_numbers(s):
    return [int(input()) for _ in range(s)]

def get_town_hill_numbers(t):
    return [int(input()) for _ in range(t)]

def calculate_aqueduct_length(hill_coordinates, spring_hill_numbers, town_hill_numbers, q):
    # Initialize variables
    spring_town_distances = {}
    town_spring_distances = {}
    aqueduct_lengths = {}
    total_length = 0

    # Calculate the distances between springs and towns
    for i in range(len(spring_hill_numbers)):
        spring_hill_number = spring_hill_numbers[i]
        town_hill_number = town_hill_numbers[i]
        spring_coordinate = hill_coordinates[spring_hill_number - 1]
        town_coordinate = hill_coordinates[town_hill_number - 1]
        spring_town_distance = math.sqrt((spring_coordinate[0] - town_coordinate[0]) ** 2 + (spring_coordinate[1] - town_coordinate[1]) ** 2)
        spring_town_distances[(spring_hill_number, town_hill_number)] = spring_town_distance
        town_spring_distances[(town_hill_number, spring_hill_number)] = spring_town_distance

    # Calculate the lengths of the aqueducts
    for spring_hill_number in spring_hill_numbers:
        for town_hill_number in town_hill_numbers:
            if (spring_hill_number, town_hill_number) in spring_town_distances:
                spring_town_distance = spring_town_distances[(spring_hill_number, town_hill_number)]
                if spring_town_distance <= q:
                    aqueduct_length = spring_town_distance
                else:
                    aqueduct_length = q
                aqueduct_lengths[(spring_hill_number, town_hill_number)] = aqueduct_length
                total_length += aqueduct_length

    return total_length

def main():
    n, s, t, q = map(int, input().split())
    hill_coordinates = get_hill_coordinates(n)
    spring_hill_numbers = get_spring_hill_numbers(s)
    town_hill_numbers = get_town_hill_numbers(t)
    total_length = calculate_aqueduct_length(hill_coordinates, spring_hill_numbers, town_hill_numbers, q)
    print(total_length)

if __name__ == '__main__':
    main()

