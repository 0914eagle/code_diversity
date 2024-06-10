
def get_lexicographically_smallest_permutations(permutations):
    
    return min(permutations)

def get_absolute_difference(a, b):
    
    return abs(a - b)

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    p_lexicographically_smallest = get_lexicographically_smallest_permutations(p)
    q_lexicographically_smallest = get_lexicographically_smallest_permutations(q)
    a = p_lexicographically_smallest.index(p) + 1
    b = q_lexicographically_smallest.index(q) + 1
    print(get_absolute_difference(a, b))

if __name__ == '__main__':
    main()

