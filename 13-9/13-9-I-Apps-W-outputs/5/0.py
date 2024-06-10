
def get_lamp_schedule(n, k):
    # Function to get the schedule of lamps
    return [(i, i % n + 1) for i in range(n)]

def get_open_doors(lamp_schedule, k):
    # Function to get the number of ways to open the door
    num_open_doors = 0
    for i in range(len(lamp_schedule)):
        for j in range(i+1, len(lamp_schedule)):
            if lamp_schedule[i][0] < lamp_schedule[j][0] < lamp_schedule[i][1]:
                num_open_doors += 1
    return num_open_doors

def main():
    n, k = map(int, input().split())
    lamp_schedule = get_lamp_schedule(n, k)
    num_open_doors = get_open_doors(lamp_schedule, k)
    print(num_open_doors % 998244353)

if __name__ == '__main__':
    main()

