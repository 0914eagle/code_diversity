
N, D = map(int, input().split())
C, *infected = map(int, input().split()[1:])
people = []
for _ in range(N):
    s, t = map(int, input().split())
    people.append((s, t))

infected_set = set(infected)
for _ in range(D):
    new_infected = set()
    for i in range(N):
        if i+1 not in infected_set:
            for j in infected_set:
                if people[j-1][0] <= people[i][1] and people[i][0] <= people[j-1][1]:
                    new_infected.add(i+1)
                    break
    infected_set.update(new_infected)

print(' '.join(map(str, sorted(infected_set))))
