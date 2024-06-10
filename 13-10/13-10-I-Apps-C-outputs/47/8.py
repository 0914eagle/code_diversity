
def is_consistent(matches):
    n = len(matches)
    skills = [0] * n
    for i in range(n):
        skill = skills[matches[i][0]]
        opp_skill = skills[matches[i][1]]
        if matches[i][2] == ">":
            skills[matches[i][0]] = skill + 1
        elif matches[i][2] == "=":
            skills[matches[i][0]] = skill + 0.5
            skills[matches[i][1]] = opp_skill + 0.5
    for i in range(n):
        if skills[i] < 0 or skills[i] > 1:
            return False
    return True

def main():
    n, m = map(int, input().split())
    matches = []
    for i in range(m):
        match = list(map(int, input().split()))
        matches.append(match)
    if is_consistent(matches):
        print("consistent")
    else:
        print("inconsistent")

if __name__ == '__main__':
    main()

