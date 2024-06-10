
def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

def is_possible(n, a):
    if n == 1:
        return True
    
    if a[1] == 0:
        return False
    
    return is_possible(n-1, a[1:])

def get_output(n, a):
    if not is_possible(n, a):
        return -1
    
    messages = []
    for i in range(1, n+1):
        if a[i] > 0:
            messages.append((1, i))
            a[i] -= 1
    
    return len(messages), messages

def main():
    n, a = get_input()
    k, messages = get_output(n, a)
    print(k)
    for message in messages:
        print(*message)

if __name__ == '__main__':
    main()

