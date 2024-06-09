
def f1(N, M):
    # Initialize the playing fields with random integers between 1 and N
    fields = [(i % N) + 1 for i in range(M)]
    # Initialize the integers of the players with random integers between 1 and N
    integers = [(i % N) + 1 for i in range(N)]
    # Assign each playing field a unique integer
    for i in range(M):
        fields[i] = integers[i]
    return fields

def f2(N, M):
    # Initialize the playing fields with random integers between 1 and N
    fields = [(i % N) + 1 for i in range(M)]
    # Initialize the integers of the players with random integers between 1 and N
    integers = [(i % N) + 1 for i in range(N)]
    # Assign each playing field a unique integer
    for i in range(M):
        fields[i] = integers[i]
    return fields

if __name__ == '__main__':
    N, M = map(int, input().split())
    fields = f1(N, M)
    for field in fields:
        print(*field)

