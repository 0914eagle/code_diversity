
def get_dream_duration(n, s):
    durations = []
    for i in range(n):
        if s[i] == "U":
            durations.append(i + 1)
        else:
            durations.append(n - i)
    return durations

def main():
    n = int(input())
    s = input()
    durations = get_dream_duration(n, s)
    print(*durations, sep=" ")

if __name__ == '__main__':
    main()

