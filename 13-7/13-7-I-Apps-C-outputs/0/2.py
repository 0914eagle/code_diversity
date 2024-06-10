
import math

def get_bug_probabilities(bugs, hours, f):
    
    bug_probabilities = []
    for bug in bugs:
        bug_probabilities.append([])
        for hour in range(hours):
            if hour == 0:
                bug_probabilities[-1].append(bug[0])
            else:
                bug_probabilities[-1].append(bug_probabilities[-1][-1] * f)
    return bug_probabilities

def get_bug_severities(bugs):
    
    return [bug[1] for bug in bugs]

def get_expected_severity(bug_probabilities, bug_severities):
    
    expected_severity = 0
    for i in range(len(bug_probabilities)):
        expected_severity += bug_severities[i] * bug_probabilities[i][-1]
    return expected_severity

def main():
    bugs, hours, f = map(int, input().split())
    bug_probabilities = get_bug_probabilities([tuple(map(float, input().split())) for _ in range(bugs)], hours, f)
    bug_severities = get_bug_severities([tuple(map(int, input().split())) for _ in range(bugs)])
    print(round(get_expected_severity(bug_probabilities, bug_severities), 6))

if __name__ == '__main__':
    main()

