
def get_beauty(permutation, n):
    beauty = 0
    for i in range(n):
        beauty += (i ^ permutation[i])
    return beauty

def get_max_beauty_permutation(n):
    permutation = list(range(n))
    max_beauty = get_beauty(permutation, n)
    for i in range(n):
        for j in range(i+1, n):
            permutation[i], permutation[j] = permutation[j], permutation[i]
            beauty = get_beauty(permutation, n)
            if beauty > max_beauty:
                max_beauty = beauty
                max_permutation = permutation[:]
            permutation[i], permutation[j] = permutation[j], permutation[i]
    return max_beauty, max_permutation

if __name__ == '__main__':
    n = int(input())
    max_beauty, max_permutation = get_max_beauty_permutation(n)
    print(max_beauty)
    print(*max_permutation)

