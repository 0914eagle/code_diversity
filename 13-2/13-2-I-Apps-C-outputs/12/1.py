
def f1(k, answers):
    # find the longest subsequence of length at least k with the highest success rate
    max_success_rate = 0
    best_subsequence = []
    for i in range(len(answers) - k + 1):
        subsequence = answers[i:i+k]
        success_rate = subsequence.count("1") / len(subsequence)
        if success_rate > max_success_rate:
            max_success_rate = success_rate
            best_subsequence = subsequence
    return best_subsequence

def f2(k, answers):
    # find the subsequence with the highest success rate that is at least k long
    max_success_rate = 0
    best_subsequence = []
    for i in range(len(answers) - k + 1):
        for j in range(i+k, len(answers)+1):
            subsequence = answers[i:j]
            success_rate = subsequence.count("1") / len(subsequence)
            if success_rate > max_success_rate:
                max_success_rate = success_rate
                best_subsequence = subsequence
    return best_subsequence

if __name__ == '__main__':
    k = int(input())
    answers = input()
    print(f1(k, answers))
    print(f2(k, answers))

