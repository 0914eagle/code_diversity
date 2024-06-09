
def get_binary_representation(n, k):
    return bin(n)[2:].zfill(k)

def get_potential_friends(n, m, k, armies):
    potential_friends = 0
    for i in range(m):
        for j in range(i + 1, m + 1):
            if hamming_distance(armies[i], armies[j]) <= k:
                potential_friends += 1
    return potential_friends

def hamming_distance(n, m):
    return bin(n ^ m).count("1")

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    armies = []
    for i in range(m + 1):
        armies.append(int(input()))
    print(get_potential_friends(n, m, k, armies))

