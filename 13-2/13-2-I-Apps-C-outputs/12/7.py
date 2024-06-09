
def f1(k, answers):
    # find the longest substring of correct answers
    longest_substring = 0
    current_substring = 0
    for i in range(len(answers)):
        if answers[i] == "1":
            current_substring += 1
        else:
            longest_substring = max(longest_substring, current_substring)
            current_substring = 0
    longest_substring = max(longest_substring, current_substring)

    # find the first index of the longest substring
    first_index = 0
    for i in range(len(answers)):
        if answers[i] == "1":
            first_index = i
            break

    return first_index + 1, longest_substring

def f2(k, answers):
    # find the longest substring of correct answers
    longest_substring = 0
    current_substring = 0
    for i in range(len(answers)):
        if answers[i] == "1":
            current_substring += 1
        else:
            longest_substring = max(longest_substring, current_substring)
            current_substring = 0
    longest_substring = max(longest_substring, current_substring)

    # find the first index of the longest substring
    first_index = 0
    for i in range(len(answers)):
        if answers[i] == "1":
            first_index = i
            break

    return first_index + 1, longest_substring

if __name__ == '__main__':
    k = int(input())
    answers = input()
    print(f1(k, answers))

