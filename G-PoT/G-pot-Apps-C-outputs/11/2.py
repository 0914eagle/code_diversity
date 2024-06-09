
import sys

def read_input():
    t, n = map(int, input().split())
    questions = []
    for _ in range(n):
        question, answer = input().split('?')
        questions.append((question.strip(), answer.strip()))
    return t, questions

def calculate_expected_score(t, questions):
    total_score = 0
    for question, answer in questions:
        words = question.split()
        time_to_answer = len(words) + 1  # Time to answer is number of words + 1
        prob_correct = 1 / time_to_answer
        total_score += prob_correct
    return total_score

def main():
    t, questions = read_input()
    expected_score = calculate_expected_score(t, questions)
    print("{:.10f}".format(expected_score))

if __name__ == "__main__":
    main()
