
def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

def get_possible_messages(n, a):
    messages = []
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j and a[i-1] > 0 and j not in messages:
                messages.append(j)
                a[i-1] -= 1
                if a[i-1] == 0:
                    break
    return messages

def get_output(n, a, messages):
    if len(messages) == 0:
        return -1
    else:
        output = []
        for i in range(1, n+1):
            for j in messages:
                if i != j:
                    output.append([i, j])
        return output

def main():
    n, a = get_input()
    messages = get_possible_messages(n, a)
    output = get_output(n, a, messages)
    print(len(output))
    for i, j in output:
        print(i, j)

if __name__ == '__main__':
    main()

