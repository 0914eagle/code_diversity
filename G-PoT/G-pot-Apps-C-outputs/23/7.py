
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
            s, t = people[i]
            if any(j in infected_set for j in range(max(1, i-50), min(N, i+51))):
                new_infected.add(i+1)
    infected_set |= new_infected

print(' '.join(map(str, sorted(infected_set))))
