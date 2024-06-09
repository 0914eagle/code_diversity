
def get_input():
    N = int(input())
    V = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    return N, V, A, B

def get_supervisors(A, B):
    supervisors = set()
    for a, b in zip(A, B):
        supervisors.add(a)
        supervisors.add(b)
    return supervisors

def get_jokes(V, supervisors):
    jokes = set()
    for v in V:
        if v in supervisors:
            jokes.add(v)
    return jokes

def get_consecutive_jokes(jokes):
    consecutive_jokes = []
    for i in range(len(jokes)):
        if i == 0:
            consecutive_jokes.append(jokes[i])
        else:
            if jokes[i] - jokes[i-1] == 1:
                consecutive_jokes.append(jokes[i])
            else:
                consecutive_jokes = []
        if i == len(jokes) - 1 and len(consecutive_jokes) > 0:
            consecutive_jokes.append(jokes[i])
    return consecutive_jokes

def get_unique_jokes(jokes):
    unique_jokes = set()
    for joke in jokes:
        unique_jokes.add(joke)
    return len(unique_jokes)

def main():
    N, V, A, B = get_input()
    supervisors = get_supervisors(A, B)
    jokes = get_jokes(V, supervisors)
    consecutive_jokes = get_consecutive_jokes(jokes)
    unique_jokes = get_unique_jokes(consecutive_jokes)
    print(unique_jokes)

if __name__ == '__main__':
    main()

