
N = int(input())
S = input().split()

C_0 = S.count("AC")
C_1 = S.count("WA")
C_2 = S.count("TLE")
C_3 = S.count("RE")

print("AC x", C_0)
print("WA x", C_1)
print("TLE x", C_2)
print("RE x", C_3)

