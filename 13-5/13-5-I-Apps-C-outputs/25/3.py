
def f1(N, dictionary):
    # your code here
    return dictionary

def f2(Q, queries):
    # your code here
    return queries

if __name__ == '__main__':
    N = int(input())
    dictionary = []
    for i in range(N):
        dictionary.append(input())
    Q = int(input())
    queries = []
    for i in range(Q):
        queries.append(input())
    print(f1(N, dictionary))
    print(f2(Q, queries))

