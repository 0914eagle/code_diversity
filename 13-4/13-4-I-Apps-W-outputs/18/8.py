
def get_input():
    return list(map(int, input().split()))

def get_assignment(n, m):
    assignment = []
    for i in range(m):
        a, b = i % n + 1, (i + 1) % n + 1
        assignment.append([a, b])
    return assignment

def main():
    n, m = get_input()
    assignment = get_assignment(n, m)
    for a, b in assignment:
        print(a, b)

if __name__ == '__main__':
    main()

