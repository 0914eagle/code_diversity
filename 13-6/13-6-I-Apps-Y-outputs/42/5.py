
def get_triples(sticks):
    triples = []
    for i in range(len(sticks)):
        for j in range(i+1, len(sticks)):
            for k in range(j+1, len(sticks)):
                if sticks[i] != sticks[j] and sticks[j] != sticks[k] and sticks[i] != sticks[k]:
                    triples.append((i, j, k))
    return triples

def get_triangles(triples, sticks):
    triangles = 0
    for triple in triples:
        a = sticks[triple[0]]
        b = sticks[triple[1]]
        c = sticks[triple[2]]
        if a + b > c and b + c > a and a + c > b:
            triangles += 1
    return triangles

def main():
    n = int(input())
    sticks = list(map(int, input().split()))
    triples = get_triples(sticks)
    triangles = get_triangles(triples, sticks)
    print(triangles)

if __name__ == '__main__':
    main()

