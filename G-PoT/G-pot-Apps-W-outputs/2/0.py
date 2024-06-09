
d, L, v1, v2 = map(int, input().split())

max_speed = max(v1, v2)
min_speed = min(v1, v2)

time_to_meet = (L - d) / (v1 + v2)

if v1 == v2:
    print("{:.20f}".format(time_to_meet))
else:
    time_to_edge = d / (max_speed - min_speed)
    print("{:.20f}".format(max(time_to_meet, time_to_edge)))
