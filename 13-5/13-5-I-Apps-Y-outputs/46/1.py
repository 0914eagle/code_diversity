
def get_consecutive_rainy_days(S):
    max_consecutive_rainy_days = 0
    current_consecutive_rainy_days = 0
    for i in range(len(S)):
        if S[i] == "R":
            current_consecutive_rainy_days += 1
        else:
            max_consecutive_rainy_days = max(max_consecutive_rainy_days, current_consecutive_rainy_days)
            current_consecutive_rainy_days = 0
    return max(max_consecutive_rainy_days, current_consecutive_rainy_days)

def main():
    S = input()
    print(get_consecutive_rainy_days(S))

if __name__ == '__main__':
    main()

