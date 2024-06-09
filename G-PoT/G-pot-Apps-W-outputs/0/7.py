
MOD = 998244353

def mod_inverse(a):
    return pow(a, MOD-2, MOD)

def expected_damage(n, m, monsters, shields):
    total_damage = sum(monsters)
    prefix_sum = [0] * (n+1)
    for i in range(1, n+1):
        prefix_sum[i] = prefix_sum[i-1] + monsters[i-1]

    results = []
    for a, b in shields:
        expected = 0
        for i in range(n):
            damage_without_shield = max(0, monsters[i] - b)
            expected += (prefix_sum[n] - prefix_sum[i] - damage_without_shield) * mod_inverse(n)
        results.append(expected % MOD)

    return results

# Input
n, m = map(int, input().split())
monsters = list(map(int, input().split()))
shields = [list(map(int, input().split())) for _ in range(m)]

# Output
results = expected_damage(n, m, monsters, shields)
for res in results:
    print(res)

