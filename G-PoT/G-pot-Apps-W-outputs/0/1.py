
MOD = 998244353

def mod_inverse(x):
    return pow(x, MOD-2, MOD)

n, m = map(int, input().split())
monsters = list(map(int, input().split()))

for _ in range(m):
    a, b = map(int, input().split())
    total_damage = 0
    for monster in monsters:
        if monster >= b:
            total_damage += 0
        else:
            total_damage += monster * mod_inverse(a)
    print((total_damage % MOD))

