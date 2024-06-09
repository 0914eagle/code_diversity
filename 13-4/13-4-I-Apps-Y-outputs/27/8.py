
N = int(input())

ac = 0
wa = 0
tle = 0
re = 0

for i in range(N):
    verdict = input()
    if verdict == "AC":
        ac += 1
    elif verdict == "WA":
        wa += 1
    elif verdict == "TLE":
        tle += 1
    else:
        re += 1

print("AC x", ac)
print("WA x", wa)
print("TLE x", tle)
print("RE x", re)

