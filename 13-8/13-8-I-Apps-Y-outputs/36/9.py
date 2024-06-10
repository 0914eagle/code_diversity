
def read_input():
    N = int(input())
    times = []
    for i in range(N):
        times.append(int(input()))
    return times

def solve(times):
    current_time = 0
    for time in times:
        if current_time < time:
            current_time = time
        else:
            current_time += 1
    if current_time < 1000000:
        return current_time
    else:
        return "still running"

def main():
    times = read_input()
    print(solve(times))

if __name__ == '__main__':
    main()

