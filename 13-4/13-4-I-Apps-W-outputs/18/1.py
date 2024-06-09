
def get_assignment(n, m):
    assignment = []
    for i in range(m):
        a = i % n + 1
        b = (i + 1) % n + 1
        assignment.append([a, b])
    return assignment

def main():
    n, m = map(int, input().split())
    assignment = get_assignment(n, m)
    for a, b in assignment:
        print(a, b)

if __name__ == '__main__':
    main()

