
def get_recorders_required(programs):
    channels = set()
    for program in programs:
        channels.add(program[2])
    return len(channels)

def get_programs(n, c):
    programs = []
    for i in range(n):
        s, t, c = map(int, input().split())
        programs.append((s, t, c))
    return programs

if __name__ == '__main__':
    n, c = map(int, input().split())
    programs = get_programs(n, c)
    print(get_recorders_required(programs))

