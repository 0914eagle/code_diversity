
def get_noise(t):
    noise = 0
    for i in range(len(t) - 1):
        if t[i] == "s" and t[i + 1] == "h":
            noise += 1
    return noise

def get_max_noise(t_list):
    max_noise = 0
    for i in range(len(t_list)):
        for j in range(i + 1, len(t_list)):
            t = t_list[i] + t_list[j]
            noise = get_noise(t)
            if noise > max_noise:
                max_noise = noise
    return max_noise

def main():
    n = int(input())
    t_list = []
    for i in range(n):
        t_list.append(input())
    print(get_max_noise(t_list))

if __name__ == '__main__':
    main()

