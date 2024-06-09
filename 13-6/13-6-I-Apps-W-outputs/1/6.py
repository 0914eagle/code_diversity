
def find_time(total_time, monkeys_1, monkeys_2):
    # Find the time when the second type of monkey arrives
    time_1 = 0
    time_2 = 0
    for i in range(len(monkeys_1)):
        time_1 += monkeys_1[i][0] + (monkeys_1[i][1] - 1) * monkeys_1[i][0]
    for i in range(len(monkeys_2)):
        time_2 += monkeys_2[i][0] + (monkeys_2[i][1] - 1) * monkeys_2[i][0]
    return total_time - max(time_1, time_2)

def main():
    total_time = int(input())
    num_monkeys_1 = int(input())
    monkeys_1 = []
    for i in range(num_monkeys_1):
        monkeys_1.append(list(map(int, input().split())))
    num_monkeys_2 = int(input())
    monkeys_2 = []
    for i in range(num_monkeys_2):
        monkeys_2.append(list(map(int, input().split())))
    print(find_time(total_time, monkeys_1, monkeys_2))

if __name__ == '__main__':
    main()

