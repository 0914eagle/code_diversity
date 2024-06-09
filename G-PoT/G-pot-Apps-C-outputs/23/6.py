
from collections import defaultdict

def get_infected_people(N, D, C, infected, entries):
    contacts = defaultdict(set)
    infected_set = set(infected)
    
    for day in range(D):
        for i in range(N):
            if i+1 not in infected_set:
                for j in range(i+1, N):
                    if j+1 in infected_set:
                        if entries[i][0] <= entries[j][1] and entries[j][0] <= entries[i][1]:
                            contacts[i+1].add(j+1)
                            contacts[j+1].add(i+1)
        
        new_infected = set()
        for person in contacts:
            if person in infected_set:
                new_infected.update(contacts[person])
        
        infected_set.update(new_infected)
    
    return sorted(list(infected_set))

# Read input
N, D = map(int, input().split())
C, *infected = map(int, input().split())
entries = [tuple(map(int, input().split())) for _ in range(N)]

# Get infected people after D days
result = get_infected_people(N, D, C, infected, entries)

# Print output
print(' '.join(map(str, result)))
