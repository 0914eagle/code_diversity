
def is_possible(participants, first_encounters):
    # Initialize a graph with participants as nodes
    graph = {participant: set() for participant in participants}

    # Add edges to the graph based on first encounters
    for participant1, participant2, year in first_encounters:
        graph[participant1].add(participant2)
        graph[participant2].add(participant1)

    # Find the year with the maximum number of first encounters
    max_year = max(year for _, _, year in first_encounters)

    # Initialize the set of participants who have met in the current year
    current_year_participants = set(participants)

    # Iterate through the years from 1948 to 2007 (inclusive)
    for year in range(1948, 2008):
        # If the current year is the maximum year, break the loop
        if year == max_year:
            break

        # Find the participants who have met in the current year
        current_year_participants = set.union(*[graph[participant] for participant in current_year_participants])

        # If the number of participants in the current year is more than 2/3 of the total number of participants, return 'Impossible'
        if len(current_year_participants) > 2 * len(participants) // 3:
            return 'Impossible'

    # If the loop completes successfully, return the maximum year
    return max_year

def main():
    n, c = map(int, input().split())
    first_encounters = []
    for _ in range(c):
        participant1, participant2, year = map(int, input().split())
        first_encounters.append((participant1, participant2, year))
    print(is_possible(range(1, n + 1), first_encounters))

if __name__ == '__main__':
    main()

