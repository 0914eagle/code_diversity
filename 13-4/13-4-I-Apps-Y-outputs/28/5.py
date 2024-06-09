
def get_two_grams(s):
    two_grams = []
    for i in range(len(s) - 1):
        two_grams.append(s[i:i+2])
    return two_grams

def get_most_frequent_two_gram(s):
    two_grams = get_two_grams(s)
    frequency = {}
    for two_gram in two_grams:
        if two_gram in frequency:
            frequency[two_gram] += 1
        else:
            frequency[two_gram] = 1
    max_frequency = max(frequency.values())
    for two_gram, count in frequency.items():
        if count == max_frequency:
            return two_gram

def main():
    n = int(input())
    s = input()
    print(get_most_frequent_two_gram(s))

if __name__ == '__main__':
    main()

