
n = int(input())
buttons = [[] for _ in range(n)]
for i in range(n):
    line = input()
    for j, c in enumerate(line):
        if c == "Y":
            buttons[j].append(i)

def get_valid_assignments(assignments):
    for i in range(n):
        for j in range(i+1, n):
            if assignments[i] == assignments[j]:
                return False
    return True

def get_max_assignments(assignments):
    max_assignments = []
    for i in range(n):
        for j in range(n):
            if get_valid_assignments(assignments + [j]):
                max_assignments.append(assignments + [j])
    return max_assignments

def get_output(assignments):
    output = ""
    for i in range(n):
        output += str(assignments[i] + 1) + " "
    return output.strip()

assignments = []
max_assignments = get_max_assignments(assignments)
print(len(max_assignments))
for assignment in max_assignments:
    print(get_output(assignment))

