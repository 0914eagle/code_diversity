
def generate_smallest_string(n, k):
    if n < k or (n > 1 and k == 1):
        return "-1"
    
    result = ""
    for i in range(k):
        result += chr(ord('a') + i) * 2
    
    if len(result) < n:
        result += chr(ord('a') + k)
    
    return result[:n]

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(generate_smallest_string(n, k))
