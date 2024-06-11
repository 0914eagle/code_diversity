def odd_count(lst):
    
    return [f"the number of odd elements {sum(int(i) % 2 for i in s)}n the str{len(s)}ng {len(s)} of the {len(s)}nput." for s in lst]
/Python/Python_codes/p03475/s418788641.py
N = int(input())
C = [0]*N
S = [0]*N
F = [0]*N
for i in range(N-1):
    C[i], S[i], F[i] = map(int, input().split())

for i in range(N-1):
    t = S[i]
    for j in range(i+1, N-1):
        if t < S[j]:
            t = S[j]
        elif t % F[j] != 0:
            t += F[j] - t % F[j]
        t += C[j]
    print(t)
print(0)/Python_codes/p02768/s359157776.py
