
def add_to_set(S, x):
    S.append(x)
    S.sort()
    return S

def find_subset(S):
    max_value = max(S)
    mean = sum(S) / len(S)
    subset = [x for x in S if x <= mean]
    return max_value - mean

if __name__ == '__main__':
    Q = int(input())
    S = []
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            x = int(query[1])
            S = add_to_set(S, x)
        else:
            print(find_subset(S))

