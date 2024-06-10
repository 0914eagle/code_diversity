
import math

def check_match_fit(W, H, match_length):
    diagonal_length = math.sqrt(W**2 + H**2)
    if match_length <= diagonal_length:
        return "DA"
    else:
        return "NE"

if __name__ == "__main__":
    N, W, H = map(int, input().split())
    for _ in range(N):
        match_length = int(input())
        result = check_match_fit(W, H, match_length)
        print(result)
