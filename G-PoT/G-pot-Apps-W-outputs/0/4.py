
MOD = 998244353

def mod_inv(x):
    return pow(x, MOD-2, MOD)

n, m = map(int, input().split())
monsters = list(map(int, input().split()))

for _ in range(m):
    a, b = map(int, input().split())
    total_damage = 0
    for monster in monsters:
        if a == 0:
            total_damage += monster
        elif monster >= b:
            total_damage += 0
            a -= 1
        else:
            total_damage += 0
    print((total_damage * mod_inv(n)) % MOD)
