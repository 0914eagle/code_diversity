
def get_noise(string):
    noise = 0
    for i in range(len(string) - 1):
        if string[i] == 's' and string[i + 1] == 'h':
            noise += 1
    return noise

def get_max_noise(strings):
    max_noise = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            noise = get_noise(strings[i] + strings[j])
            if noise > max_noise:
                max_noise = noise
    return max_noise

def main():
    n = int(input())
    strings = []
    for i in range(n):
        strings.append(input())
    print(get_max_noise(strings))

if __name__ == '__main__':
    main()

