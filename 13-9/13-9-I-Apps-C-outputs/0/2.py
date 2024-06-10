
def get_battery_powers(n, k):
    powers = []
    for i in range(2*n*k):
        powers.append(int(input()))
    return powers

def get_optimal_allocation(powers, n, k):
    batteries_per_machine = k*2
    allocated_batteries = []
    for i in range(n):
        machine_batteries = sorted(powers[i*batteries_per_machine:(i+1)*batteries_per_machine])
        allocated_batteries += machine_batteries[:k]
        allocated_batteries += machine_batteries[k:]
    return allocated_batteries

def get_difference(allocated_batteries, n, k):
    differences = []
    for i in range(n):
        machine_batteries = allocated_batteries[i*k:(i+1)*k]
        differences.append(abs(machine_batteries[0] - machine_batteries[1]))
    return min(differences)

def main():
    n, k = map(int, input().split())
    powers = get_battery_powers(n, k)
    allocated_batteries = get_optimal_allocation(powers, n, k)
    difference = get_difference(allocated_batteries, n, k)
    print(difference)

if __name__ == '__main__':
    main()

