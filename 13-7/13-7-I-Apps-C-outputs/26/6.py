
def get_matching_pairs(num_languages, num_translators, translators):
    # Initialize a dictionary to store the pairs of translators who speak the same language
    pairs = {}
    for i in range(num_languages):
        pairs[i] = []
    
    # Iterate through the translators and add them to the dictionary
    for translator in translators:
        language1 = translator[0]
        language2 = translator[1]
        pairs[language1].append(translator[2])
        pairs[language2].append(translator[2])
    
    # Initialize a list to store the pairs of translators who speak the same language
    matched_pairs = []
    
    # Iterate through the dictionary and find pairs of translators who speak the same language
    for key, value in pairs.items():
        if len(value) > 1:
            for i in range(len(value)):
                for j in range(i+1, len(value)):
                    matched_pairs.append([value[i], value[j]])
    
    # If there are an odd number of translators, it is not possible to match them up
    if len(matched_pairs) % 2 == 1:
        return "impossible"
    
    # Otherwise, return the pairs of translators who speak the same language
    return matched_pairs

def main():
    num_languages, num_translators = map(int, input().split())
    translators = []
    for _ in range(num_translators):
        translators.append(list(map(int, input().split())))
    print(get_matching_pairs(num_languages, num_translators, translators))

if __name__ == '__main__':
    main()

