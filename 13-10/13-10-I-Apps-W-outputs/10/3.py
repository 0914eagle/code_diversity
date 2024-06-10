
def parse_input(input_str):
    n = int(input_str[0])
    s = input_str[1]
    return n, s

def get_dream_duration(n, s):
    durations = []
    for i in range(n):
        if s[i] == 'U':
            durations.append(i + 1)
        else:
            durations.append(n - i)
    return durations

def get_answer(n, s):
    durations = get_dream_duration(n, s)
    answer = []
    for i in range(n):
        if s[i] == 'U' and i == 0:
            answer.append(-1)
        elif s[i] == 'D' and i == n - 1:
            answer.append(-1)
        else:
            answer.append(durations[i - 1])
    return answer

def main():
    input_str = "3 UUD"
    n, s = parse_input(input_str)
    answer = get_answer(n, s)
    print(answer)

if __name__ == '__main__':
    main()

