
def get_battery_power_outputs(n, k):
    power_outputs = []
    for i in range(n):
        for j in range(k):
            power_outputs.append(int(input()))
    return power_outputs

def get_min_power_difference(power_outputs):
    min_power_difference = float('inf')
    for i in range(len(power_outputs) - 1):
        for j in range(i + 1, len(power_outputs)):
            power_difference = abs(power_outputs[i] - power_outputs[j])
            if power_difference < min_power_difference:
                min_power_difference = power_difference
    return min_power_difference

def main():
    n, k = map(int, input().split())
    power_outputs = get_battery_power_outputs(n, k)
    min_power_difference = get_min_power_difference(power_outputs)
    print(min_power_difference)

if __name__ == '__main__':
    main()

