
def infected_people(N, D, C, infected_indices, people):
    infected = set(infected_indices)
    contacts = [set() for _ in range(D+1)]
    
    for i in range(N):
        for j in range(i+1, N):
            if people[i][1] >= people[j][0] and people[j][1] >= people[i][0]:
                contacts[0].add((i+1, j+1))
    
    for day in range(1, D+1):
        for contact in contacts[day-1]:
            for i in range(N):
                if i+1 not in infected:
                    if any(people[i][0] <= people[j-1][1] and people[j-1][0] <= people[i][1] for j in contact):
                        contacts[day].add((i+1, contact[0][1]))
    
    for day in range(1, D+1):
        for contact in contacts[day]:
            infected.add(contact[0])
    
    return sorted(infected)

# Input parsing
N, D = map(int, input().split())
C, *infected_indices = map(int, input().split())
people = [tuple(map(int, input().split())) for _ in range(N)]

# Call the function and print the output
result = infected_people(N, D, C, infected_indices, people)
print(" ".join(map(str, result)))
