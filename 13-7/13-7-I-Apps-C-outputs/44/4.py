
def solve(n, star_systems, e, links):
    # Initialize the minimum UW distance
    min_uw_distance = float('inf')
    # Loop through each star system as the source system
    for source_system in range(n):
        # If the source system is alien, skip it
        if star_systems[source_system] == 'a':
            continue
        # Loop through each star system as the destination system
        for destination_system in range(n):
            # If the destination system is human, skip it
            if star_systems[destination_system] == 'h':
                continue
            # If the source and destination systems are the same, skip it
            if source_system == destination_system:
                continue
            # Calculate the UW distance between the source and destination systems
            uw_distance = calculate_uw_distance(source_system, destination_system, star_systems, links)
            # If the UW distance is less than the minimum UW distance, update the minimum UW distance
            if uw_distance < min_uw_distance:
                min_uw_distance = uw_distance
    # Return the minimum UW distance
    return min_uw_distance

def calculate_uw_distance(source_system, destination_system, star_systems, links):
    # Initialize the UW distance
    uw_distance = 0
    # If the source and destination systems are directly linked, return the UW distance between them
    if source_system in links[destination_system]:
        return links[destination_system][source_system]
    # If the source and destination systems are not directly linked, calculate the UW distance between them through intermediary systems
    else:
        # Loop through each intermediary system
        for intermediary_system in range(len(links)):
            # If the intermediary system is not directly linked to the source system, skip it
            if intermediary_system not in links[source_system]:
                continue
            # If the intermediary system is directly linked to the destination system, calculate the UW distance between the source and destination systems through the intermediary system
            if intermediary_system in links[destination_system]:
                uw_distance += links[intermediary_system][source_system] + links[intermediary_system][destination_system]
        # Return the UW distance
        return uw_distance

def main():
    # Read the input
    n = int(input())
    star_systems = []
    for i in range(n):
        star_systems.append(input())
    e = int(input())
    links = {}
    for i in range(e):
        source_system, destination_system = map(int, input().split())
        if source_system not in links:
            links[source_system] = {}
        links[source_system][destination_system] = int(input())
    # Solve the problem
    min_uw_distance = solve(n, star_systems, e, links)
    # Print the result
    print(min_uw_distance)

if __name__ == '__main__':
    main()

