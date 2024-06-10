
def lexicographically_smaller(p1, p2):
    for i in range(len(p1)):
        if p1[i] != p2[i]:
            return p1[i] < p2[i]
    return False

def get_lexicographical_index(permutation, permutations):
    index = 1
    for p in permutations:
        if lexicographically_smaller(permutation, p):
            index += 1
    return index

def get_absolute_difference(p1, p2):
    return abs(get_lexicographical_index(p1, p1) - get_lexicographical_index(p2, p1))

def main():
    n = int(input())
    p1 = list(map(int, input().split()))
    p2 = list(map(int, input().split()))
    print(get_absolute_difference(p1, p2))

if __name__ == '__main__':
    main()

