
# Read input
N, D = map(int, input().split())
C, *infected = map(int, input().split()[1:])
times = [list(map(int, input().split())) for _ in range(N)]

# Initialize set to store infected people
infected_set = set(infected)

# Loop through each day
for _ in range(D):
    contacts = set()
    for i in range(N):
        if i + 1 not in infected_set:
            for j in range(N):
                if i != j:
                    if times[i][0] <= times[j][1] and times[i][1] >= times[j][0]:
                        contacts.add(i + 1)
                        break
    infected_set.update(contacts)

# Print the infected people after D days
print(' '.join(map(str, sorted(infected_set))))
