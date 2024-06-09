
def spread_virus(N, D, C, infected_people, entries_exits):
    infected = set(infected_people)
    contacts = {}
    
    for day in range(D):
        new_infected = set()
        for person in range(1, N+1):
            if person in infected:
                continue
            for infected_person in infected:
                if (entries_exits[infected_person-1][0] <= entries_exits[person-1][1] and entries_exits[infected_person-1][1] >= entries_exits[person-1][0]) or (entries_exits[person-1][0] == entries_exits[person-1][1]):
                    new_infected.add(person)
                    break
        infected.update(new_infected)
    
    return sorted(list(infected))

# Read input
N, D = map(int, input().split())
C, *infected_people = map(int, input().split())
entries_exits = [list(map(int, input().split())) for _ in range(N)]

# Call the function and print the output
result = spread_virus(N, D, C, infected_people, entries_exits)
print(*result)
