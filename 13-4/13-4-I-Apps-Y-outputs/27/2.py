
N = int(input())
S = [input() for _ in range(N)]

counts = [0, 0, 0, 0]
for s in S:
    if s == "AC":
        counts[0] += 1
    elif s == "WA":
        counts[1] += 1
    elif s == "TLE":
        counts[2] += 1
    else:
        counts[3] += 1

print("AC x", counts[0])
print("WA x", counts[1])
print("TLE x", counts[2])
print("RE x", counts[3])

