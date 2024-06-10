
def get_battery_power_outputs(n, k, batteries):
    # Your code here
    return batteries

def get_difference(battery_power_outputs):
    # Your code here
    return difference

def get_optimal_allocation(n, k, batteries):
    # Your code here
    return allocation

if __name__ == '__main__':
    n, k = map(int, input().split())
    batteries = list(map(int, input().split()))
    battery_power_outputs = get_battery_power_outputs(n, k, batteries)
    difference = get_difference(battery_power_outputs)
    allocation = get_optimal_allocation(n, k, batteries)
    print(difference)

