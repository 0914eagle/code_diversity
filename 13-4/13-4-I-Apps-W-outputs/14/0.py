
def get_painting_times(n_painters, n_pictures, painting_times):
    painting_times = [[0] + painting_times[i] for i in range(n_painters)]
    painting_times = [painting_times[i] + [0] for i in range(n_painters)]
    painting_times = [painting_times[i] + painting_times[i - 1] for i in range(1, n_painters + 1)]
    return painting_times[-1]

def get_ready_times(n_painters, n_pictures, painting_times):
    painting_times = get_painting_times(n_painters, n_pictures, painting_times)
    ready_times = [painting_times[i] for i in range(n_painters, n_painters + n_pictures)]
    return ready_times

if __name__ == '__main__':
    n_painters, n_pictures = map(int, input().split())
    painting_times = []
    for i in range(n_painters):
        painting_times.append(list(map(int, input().split())))
    ready_times = get_ready_times(n_painters, n_pictures, painting_times)
    print(*ready_times, sep=' ')

