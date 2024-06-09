
def get_infected_people(N, D, C, infected_indices, people_times):
    infected = set(infected_indices)
    contacts = [[] for _ in range(D+1)]

    for i in range(N):
        for j in range(i+1, N):
            if people_times[i][1] >= people_times[j][0] and people_times[j][1] >= people_times[i][0]:
                contacts[0].append((i+1, j+1))

    for day in range(1, D+1):
        for contact in contacts[day-1]:
            for i in range(N):
                if i+1 not in infected:
                    if people_times[i][0] <= day and people_times[i][1] >= day:
                        contacts[day].append((contact[0], i+1))
                        contacts[day].append((contact[1], i+1))
                        infected.add(i+1)

    return sorted(infected)

# Read input
N, D = map(int, input().split())
C, *infected_indices = map(int, input().split())
people_times = [tuple(map(int, input().split())) for _ in range(N)]

# Get infected people after D days
infected_people = get_infected_people(N, D, C, infected_indices, people_times)

# Print output
print(' '.join(map(str, infected_people)))
