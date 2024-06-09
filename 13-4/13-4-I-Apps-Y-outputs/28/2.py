
def get_two_grams(s):
    two_grams = []
    for i in range(len(s) - 1):
        two_grams.append(s[i:i+2])
    return two_grams

def get_most_frequent_two_gram(two_grams):
    freq = {}
    for two_gram in two_grams:
        if two_gram in freq:
            freq[two_gram] += 1
        else:
            freq[two_gram] = 1
    max_freq = max(freq.values())
    for two_gram, count in freq.items():
        if count == max_freq:
            return two_gram

def main():
    n = int(input())
    s = input()
    two_grams = get_two_grams(s)
    most_frequent_two_gram = get_most_frequent_two_gram(two_grams)
    print(most_frequent_two_gram)

if __name__ == '__main__':
    main()

