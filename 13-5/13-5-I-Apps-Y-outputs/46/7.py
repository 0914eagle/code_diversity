
def get_max_consecutive_rainy_days(S):
    max_count = 0
    current_count = 0
    for i in range(len(S)):
        if S[i] == "R":
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 0
    return max_count

def main():
    S = input()
    print(get_max_consecutive_rainy_days(S))

if __name__ == '__main__':
    main()

