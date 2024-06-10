
def count_correct_forecasts(S, T):
    count = 0
    for i in range(3):
        if S[i] == T[i]:
            count += 1
    return count

if __name__ == "__main__":
    S = input().strip()
    T = input().strip()
    print(count_correct_forecasts(S, T))
