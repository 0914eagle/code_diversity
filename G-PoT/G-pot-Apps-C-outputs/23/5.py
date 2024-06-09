
def get_infected_people(N, D, C, infected_indices, entries_exits):
    infected = set(infected_indices)
    contacts = set()
    
    for _ in range(D):
        new_infected = set()
        for i in range(N):
            if i + 1 not in infected:
                for j in infected:
                    if entries_exits[j-1][0] <= entries_exits[i][1] and entries_exits[j-1][1] >= entries_exits[i][0]:
                        new_infected.add(i + 1)
                        break
        infected.update(new_infected)
    
    return sorted(list(infected))

# Read input
N, D = map(int, input().split())
C, *infected_indices = map(int, input().split())
entries_exits = [list(map(int, input().split())) for _ in range(N)]

# Get infected people after D days
infected_people = get_infected_people(N, D, C, infected_indices, entries_exits)

# Print output
print(' '.join(map(str, infected_people)))
