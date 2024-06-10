
def get_battery_power(batteries):
    return sorted(batteries)[0]

def get_difference(machines, batteries):
    differences = []
    for machine in machines:
        differences.append(abs(get_battery_power(machine[0]) - get_battery_power(machine[1])))
    return sorted(differences)[0]

def get_optimized_allocation(machines, batteries):
    optimized_allocation = []
    for machine in machines:
        optimized_allocation.append([batteries.pop(0) for _ in range(2)])
    return optimized_allocation

def main():
    num_machines, num_batteries_per_machine = map(int, input().split())
    batteries = list(map(int, input().split()))
    machines = [[batteries.pop(0) for _ in range(num_batteries_per_machine)] for _ in range(num_machines)]
    difference = get_difference(machines, batteries)
    optimized_allocation = get_optimized_allocation(machines, batteries)
    print(difference)

if __name__ == '__main__':
    main()

