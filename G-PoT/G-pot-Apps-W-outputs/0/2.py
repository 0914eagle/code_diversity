
MOD = 998244353

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

n, m = map(int, input().split())
monsters = list(map(int, input().split()))
shields = []
for _ in range(m):
    a, b = map(int, input().split())
    shields.append((a, b))

for shield in shields:
    a, b = shield
    total_damage = 0
    for monster in monsters:
        if a == 0:
            total_damage += monster
        elif monster >= b:
            total_damage += 0
            a -= 1
        else:
            total_damage += 0
    expected_damage = total_damage % MOD
    inverse_a = mod_inverse(a, MOD)
    result = (expected_damage * inverse_a) % MOD
    print(result)
