
def solve(k):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    result = []
    for i in range(len(alphabet)):
        for j in range(i+1, len(alphabet)):
            diff1 = abs(alphabet.index(alphabet[i]) - alphabet.index(alphabet[j]))
            diff2 = abs(alphabet.index(alphabet[j]) - alphabet.index(alphabet[i]))
            sum_diff = diff1 + diff2
            if sum_diff == k:
                result.append(alphabet[i] + alphabet[j])
    return sorted(result)[0]

