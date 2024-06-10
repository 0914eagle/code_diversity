
def generate_lexicographically_smallest_string(n, k):
    if n < k or (n > 1 and k == 1):
        return "-1"
    
    result = ""
    for i in range(k):
        result += chr(ord('a') + i) * 2
    
    remaining_length = n - 2 * k
    if remaining_length > 0:
        result += chr(ord('a') + k) * remaining_length
    
    return result

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(generate_lexicographically_smallest_string(n, k))
