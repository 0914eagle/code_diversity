
def get_infected_people(N, D, C, infected_indices, people):
    infected = set(infected_indices)
    for _ in range(D):
        new_infected = set()
        for i in range(N):
            if i + 1 not in infected:
                for j in infected:
                    if people[i][0] <= people[j-1][1] and people[i][1] >= people[j-1][0]:
                        new_infected.add(i + 1)
                        break
        infected.update(new_infected)
    
    return sorted(infected)

# Read input
N, D = map(int, input().split())
C, *infected_indices = map(int, input().split())
people = [tuple(map(int, input().split())) for _ in range(N)]

# Get infected people after D days
infected_people = get_infected_people(N, D, C, infected_indices, people)

# Print output
print(' '.join(map(str, infected_people)))
