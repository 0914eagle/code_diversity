
def get_infected_people(N, D, C, infected_indices, entries_exits):
    infected = set(infected_indices)
    contacts = [[] for _ in range(D + 1)]
    
    for i in range(N):
        for j in range(i + 1, N):
            if entries_exits[i][1] >= entries_exits[j][0] and entries_exits[j][1] >= entries_exits[i][0]:
                contacts[0].append((i + 1, j + 1))
    
    for day in range(1, D + 1):
        for contact in contacts[day - 1]:
            for i in range(N):
                if i + 1 not in infected and (entries_exits[i][0] <= entries_exits[contact[1] - 1][1] and entries_exits[contact[1] - 1][0] <= entries_exits[i][1]):
                    infected.add(i + 1)
                    for j in range(i + 1, N):
                        if entries_exits[i][1] >= entries_exits[j][0] and entries_exits[j][1] >= entries_exits[i][0]:
                            contacts[day].append((i + 1, j + 1))
    
    return sorted(list(infected))

# Read input
N, D = map(int, input().split())
C, *infected_indices = map(int, input().split())
entries_exits = [list(map(int, input().split())) for _ in range(N)]

# Get infected people after D days
infected_people = get_infected_people(N, D, C, infected_indices, entries_exits)

# Print output
print(" ".join(map(str, infected_people)))
