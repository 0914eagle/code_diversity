
def get_skis_and_gates(W, N, x, y):
    skis = []
    gates = []
    for i in range(N):
        skis.append((x[i], y[i]))
        gates.append((x[i] - W, y[i]))
    return skis, gates

def get_time_to_pass_gate(ski, gate, v_h):
    x, y = ski
    gx, gy = gate
    if x < gx:
        return float('inf')
    if x > gx + W:
        return float('inf')
    time = (gy - y) / v_h
    return time

def get_shortest_time_to_pass_all_gates(skis, gates, v_h):
    times = []
    for ski in skis:
        time = 0
        for gate in gates:
            time += get_time_to_pass_gate(ski, gate, v_h)
        times.append(time)
    return min(times)

def get_fastest_ski(skis, gates, v_h):
    times = []
    for ski in skis:
        time = get_time_to_pass_all_gates(ski, gates, v_h)
        times.append(time)
    return skis[times.index(min(times))]

def main():
    W, v_h, N = map(int, input().split())
    x = []
    y = []
    for i in range(N):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    S = int(input())
    skis = []
    for i in range(S):
        skis.append(int(input()))
    skis, gates = get_skis_and_gates(W, N, x, y)
    fastest_ski = get_fastest_ski(skis, gates, v_h)
    print(fastest_ski)

if __name__ == '__main__':
    main()

