
def encrypt_and_sort(words, key):
    # Encrypt the words using the given key
    encrypted_words = [word[key.index(word[0])] + word[1:] for word in words]
    
    # Sort the encrypted words lexicographically
    sorted_words = sorted(encrypted_words)
    
    # Check if the sorted words match the given array A
    if sorted_words == A:
        return "DA", key
    else:
        return "NE", None

def get_key(N, words, A):
    # Generate all possible keys
    keys = ["".join(perm) for perm in itertools.permutations("abcdefghijklmnopqrstuvwxyz")]
    
    # Check if any key works
    for key in keys:
        result = encrypt_and_sort(words, key)
        if result[0] == "DA":
            return result[1]
    
    # If no key works, return None
    return None

if __name__ == '__main__':
    N = int(input())
    words = [input() for _ in range(N)]
    A = [int(i) for i in input().split()]
    key = get_key(N, words, A)
    if key:
        print("DA")
        print(key)
    else:
        print("NE")

