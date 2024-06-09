
d, L, v1, v2 = map(int, input().split())

time_to_reach = L / (v1 + v2)
max_time_alive = (L - d) / max(v1, v2)

if max_time_alive < time_to_reach:
    print(max_time_alive)
else:
    print(time_to_reach)
