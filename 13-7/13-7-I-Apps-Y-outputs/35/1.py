
def get_minimum_time(N, A, B, C, D, E):
    # Initialize the number of people at each city
    people_at_city_1 = N
    people_at_city_2 = 0
    people_at_city_3 = 0
    people_at_city_4 = 0
    people_at_city_5 = 0
    people_at_city_6 = 0

    # Initialize the number of vehicles at each city
    vehicles_at_city_1 = 1
    vehicles_at_city_2 = 0
    vehicles_at_city_3 = 0
    vehicles_at_city_4 = 0
    vehicles_at_city_5 = 0
    vehicles_at_city_6 = 0

    # Initialize the minimum time required to reach City 6
    minimum_time = 0

    # Loop until all people reach City 6
    while people_at_city_6 < N:
        # Determine the number of people who can travel from City 1 to City 2 by train
        people_at_city_2 += min(people_at_city_1, A)
        people_at_city_1 -= min(people_at_city_1, A)
        vehicles_at_city_1 += 1

        # Determine the number of people who can travel from City 2 to City 3 by bus
        people_at_city_3 += min(people_at_city_2, B)
        people_at_city_2 -= min(people_at_city_2, B)
        vehicles_at_city_2 += 1

        # Determine the number of people who can travel from City 3 to City 4 by taxi
        people_at_city_4 += min(people_at_city_3, C)
        people_at_city_3 -= min(people_at_city_3, C)
        vehicles_at_city_3 += 1

        # Determine the number of people who can travel from City 4 to City 5 by airplane
        people_at_city_5 += min(people_at_city_4, D)
        people_at_city_4 -= min(people_at_city_4, D)
        vehicles_at_city_4 += 1

        # Determine the number of people who can travel from City 5 to City 6 by ship
        people_at_city_6 += min(people_at_city_5, E)
        people_at_city_5 -= min(people_at_city_5, E)
        vehicles_at_city_5 += 1

        # Increment the minimum time required to reach City 6
        minimum_time += 1

    # Return the minimum time required to reach City 6
    return minimum_time

def main():
    # Read the input
    N, A, B, C, D, E = map(int, input().split())

    # Call the get_minimum_time function
    minimum_time = get_minimum_time(N, A, B, C, D, E)

    # Print the minimum time required to reach City 6
    print(minimum_time)

if __name__ == '__main__':
    main()

