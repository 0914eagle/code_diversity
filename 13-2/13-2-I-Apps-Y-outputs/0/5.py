
blimps = []

for i in range(5):
    blimp = input()
    blimps.append(blimp)

cia_blimps = []

for i, blimp in enumerate(blimps):
    if "FBI" in blimp:
        cia_blimps.append(i+1)

if len(cia_blimps) == 0:
    print("HE GOT AWAY!")
else:
    print(" ".join(map(str, cia_blimps)))

