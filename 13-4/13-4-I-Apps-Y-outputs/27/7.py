
N = int(input())
verdicts = [input() for _ in range(N)]

ac_count = 0
wa_count = 0
tle_count = 0
re_count = 0

for verdict in verdicts:
    if verdict == "AC":
        ac_count += 1
    elif verdict == "WA":
        wa_count += 1
    elif verdict == "TLE":
        tle_count += 1
    else:
        re_count += 1

print(f"AC x {ac_count}")
print(f"WA x {wa_count}")
print(f"TLE x {tle_count}")
print(f"RE x {re_count}")

