
def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

def send_message(n, a, student, known):
    if student == 1:
        return True
    if a[student] == 0:
        return False
    if known[student]:
        a[student] -= 1
        return True
    return False

def inform_group(n, a):
    known = [False] * (n + 1)
    messages = []
    for student in range(1, n + 1):
        if send_message(n, a, student, known):
            for i in range(1, n + 1):
                if i != student and known[i]:
                    messages.append((student, i))
    return messages

def main():
    n, a = get_input()
    messages = inform_group(n, a)
    if len(messages) == 0:
        print(-1)
    else:
        print(len(messages))
        for message in messages:
            print(message[0], message[1])

if __name__ == '__main__':
    main()

