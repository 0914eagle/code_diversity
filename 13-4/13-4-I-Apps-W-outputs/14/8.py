
def get_painting_time(m, n, painters):
    painting_time = [0] * m
    for i in range(m):
        for j in range(n):
            painting_time[i] += painters[j][i]
    return painting_time

def get_ready_time(m, n, painters):
    ready_time = [0] * m
    for i in range(m):
        for j in range(n):
            ready_time[i] = max(ready_time[i], ready_time[j] + painters[j][i])
    return ready_time

def main():
    m, n = map(int, input().split())
    painters = []
    for i in range(n):
        painters.append(list(map(int, input().split())))
    painting_time = get_painting_time(m, n, painters)
    ready_time = get_ready_time(m, n, painters)
    for i in range(m):
        print(ready_time[i] + painting_time[i])

if __name__ == '__main__':
    main()

