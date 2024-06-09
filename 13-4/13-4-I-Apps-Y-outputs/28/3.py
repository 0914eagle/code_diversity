
def get_two_grams(s):
    two_grams = []
    for i in range(len(s) - 1):
        two_grams.append(s[i:i+2])
    return two_grams

def find_most_frequent_two_gram(s):
    two_grams = get_two_grams(s)
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
    print(find_most_frequent_two_gram(s))

if __name__ == '__main__':
    main()

