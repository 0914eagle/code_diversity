
def f1(k, answers):
    # find the longest substring of answers that has the highest success rate
    # a substring is a contiguous sequence of answers
    # the success rate of a substring is the number of correct answers divided by the length of the substring
    max_success_rate = 0
    best_substring = ""
    for i in range(len(answers)):
        for j in range(i, len(answers)):
            substring = answers[i:j+1]
            success_rate = substring.count("1") / len(substring)
            if success_rate > max_success_rate:
                max_success_rate = success_rate
                best_substring = substring
    # find the first occurrence of the best substring in the original answers string
    first_occurrence = answers.find(best_substring)
    return first_occurrence + 1, len(best_substring)

def f2(k, answers):
    # find the longest substring of answers that has the highest success rate
    # a substring is a contiguous sequence of answers
    # the success rate of a substring is the number of correct answers divided by the length of the substring
    max_success_rate = 0
    best_substring = ""
    for i in range(len(answers)):
        for j in range(i, len(answers)):
            substring = answers[i:j+1]
            success_rate = substring.count("1") / len(substring)
            if success_rate > max_success_rate:
                max_success_rate = success_rate
                best_substring = substring
    # find the first occurrence of the best substring in the original answers string
    first_occurrence = answers.find(best_substring)
    return first_occurrence + 1, len(best_substring)

if __name__ == '__main__':
    k = int(input())
    answers = input()
    print(f1(k, answers))
    print(f2(k, answers))

