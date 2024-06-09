
def get_sticks(n):
    sticks = []
    for i in range(n):
        length = int(input())
        sticks.append(length)
    return sticks

def get_triples(sticks):
    triples = []
    for i in range(len(sticks)):
        for j in range(i+1, len(sticks)):
            for k in range(j+1, len(sticks)):
                if sticks[i] + sticks[j] > sticks[k] and sticks[i] + sticks[k] > sticks[j] and sticks[j] + sticks[k] > sticks[i]:
                    triples.append((i, j, k))
    return triples

def count_unique_triples(triples):
    unique_triples = set()
    for triple in triples:
        unique_triples.add(frozenset(triple))
    return len(unique_triples)

def main():
    n = int(input())
    sticks = get_sticks(n)
    triples = get_triples(sticks)
    print(count_unique_triples(triples))

if __name__ == '__main__':
    main()

