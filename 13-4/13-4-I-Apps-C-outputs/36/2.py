
def read_input():
    N = int(input())
    V = list(map(int, input().split()))
    direct_supervisors = []
    for _ in range(N-1):
        direct_supervisors.append(list(map(int, input().split())))
    return N, V, direct_supervisors

def get_supervisors(direct_supervisors, person):
    supervisors = []
    for supervisor, employee in direct_supervisors:
        if employee == person:
            supervisors.append(supervisor)
    return supervisors

def get_jokes(V, direct_supervisors, person):
    jokes = set()
    for supervisor in get_supervisors(direct_supervisors, person):
        jokes |= get_jokes(V, direct_supervisors, supervisor)
    jokes.add(V[person-1])
    return jokes

def get_consecutive_jokes(jokes):
    consecutive_jokes = []
    for i in range(len(jokes)):
        if i == 0:
            consecutive_jokes.append(jokes[i])
        elif jokes[i] - jokes[i-1] == 1:
            consecutive_jokes.append(jokes[i])
        else:
            consecutive_jokes = []
    return consecutive_jokes

def get_unique_jokes(jokes):
    unique_jokes = set()
    for joke in jokes:
        unique_jokes.add(joke)
    return unique_jokes

def get_number_of_unique_jokes(N, V, direct_supervisors):
    jokes = get_jokes(V, direct_supervisors, 1)
    consecutive_jokes = get_consecutive_jokes(jokes)
    unique_jokes = get_unique_jokes(consecutive_jokes)
    return len(unique_jokes)

if __name__ == '__main__':
    N, V, direct_supervisors = read_input()
    print(get_number_of_unique_jokes(N, V, direct_supervisors))

