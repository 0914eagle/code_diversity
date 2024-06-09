
d, L, v1, v2 = map(int, input().split())

max_time = (L - d) / (v1 + v2)
print("{:.20f}".format(max_time))
