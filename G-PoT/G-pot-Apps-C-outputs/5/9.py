
Tg, Ty, Tr = map(int, input().split())
n = int(input())
observations = []
for _ in range(n):
    t, color = input().split()
    observations.append((int(t), color))

t_q, c_q = input().split()
t_q = int(t_q)

total_time = sum([Tg, Ty, Tr])
cycle_time = total_time

def get_color_at_time(t):
    t = t % cycle_time
    if 0 <= t < Tg:
        return 'green'
    elif Tg <= t < Tg + Ty:
        return 'yellow'
    else:
        return 'red'

possible_start_times = []
for t, color in observations:
    if color == c_q:
        for i in range(cycle_time):
            if get_color_at_time(t - i) == color:
                possible_start_times.append(t - i)

count = 0
for start_time in possible_start_times:
    if get_color_at_time(t_q - start_time) == c_q:
        count += 1

probability = count / len(possible_start_times)
print(probability)
