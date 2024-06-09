
MOD = 998244353

def mod_inv(x):
    return pow(x, MOD - 2, MOD)

def expected_damage(n, m, monsters, shields):
    total_damage = sum(monsters)
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + i

    for a, b in shields:
        expected_dmg = 0
        for i in range(n):
            dmg = max(0, monsters[i] - b)
            if dmg > 0:
                expected_dmg += dmg * prefix_sum[min(a, n)]
            else:
                expected_dmg += total_damage * min(a, n)
        print((expected_dmg * mod_inv(prefix_sum[n])) % MOD)

n, m = map(int, input().split())
monsters = list(map(int, input().split()))
shields = [list(map(int, input().split())) for _ in range(m)]

expected_damage(n, m, monsters, shields)
