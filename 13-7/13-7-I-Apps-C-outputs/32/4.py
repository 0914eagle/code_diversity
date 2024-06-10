
def lexicographically_sorted_subsequences(arr):
    subsequences = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)+1):
            subsequences.append(arr[i:j])
    return sorted(subsequences)

def hash_function(arr, b, m):
    hash_value = 0
    for i in range(len(arr)):
        hash_value = (hash_value * b + arr[i]) % m
    return hash_value

def main():
    n, k, b, m = map(int, input().split())
    arr = list(map(int, input().split()))
    subsequences = lexicographically_sorted_subsequences(arr)
    for i in range(k):
        print(hash_function(subsequences[i], b, m))

if __name__ == '__main__':
    main()

