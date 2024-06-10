
def read_input():
    n, k = map(int, input().split())
    batteries = list(map(int, input().split()))
    return n, k, batteries

def get_min_difference(batteries):
    batteries.sort()
    min_diff = float('inf')
    for i in range(len(batteries) - 1):
        diff = batteries[i + 1] - batteries[i]
        min_diff = min(min_diff, diff)
    return min_diff

def get_optimal_allocation(n, k, batteries):
    batteries.sort()
    allocated_batteries = []
    for i in range(n):
        allocated_batteries.append(batteries[i * k:(i + 1) * k])
    return allocated_batteries

def get_power_outputs(allocated_batteries):
    power_outputs = []
    for batteries in allocated_batteries:
        power_outputs.append(min(batteries))
    return power_outputs

def get_difference(power_outputs):
    diff = 0
    for i in range(len(power_outputs) - 1):
        diff += abs(power_outputs[i + 1] - power_outputs[i])
    return diff

def main():
    n, k, batteries = read_input()
    allocated_batteries = get_optimal_allocation(n, k, batteries)
    power_outputs = get_power_outputs(allocated_batteries)
    d = get_difference(power_outputs)
    print(d)

if __name__ == '__main__':
    main()

