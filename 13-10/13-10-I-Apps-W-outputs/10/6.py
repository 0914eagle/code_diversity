
def get_durations(n, s):
    durations = []
    for i in range(n):
        if s[i] == 'U':
            durations.append(i+1)
        else:
            durations.append(n-i)
    return durations

def main():
    n = int(input())
    s = input()
    durations = get_durations(n, s)
    for duration in durations:
        print(duration, end=" ")

if __name__ == '__main__':
    main()

