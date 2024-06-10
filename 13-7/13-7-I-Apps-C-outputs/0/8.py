
def get_bugs_info(bugs_file):
    with open(bugs_file, "r") as f:
        bugs_info = f.read().splitlines()
    bugs_count, hours_left, failure_factor = map(float, bugs_info[0].split())
    bugs = []
    for i in range(1, len(bugs_info)):
        fix_prob, severity = map(float, bugs_info[i].split())
        bugs.append((fix_prob, severity))
    return bugs_count, hours_left, failure_factor, bugs

def get_fixed_bugs(bugs_count, hours_left, failure_factor, bugs):
    fixed_bugs = []
    for i in range(bugs_count):
        fix_prob, severity = bugs[i]
        if fix_prob >= 1 or hours_left == 0:
            fixed_bugs.append(severity)
        else:
            if np.random.uniform(0, 1) <= fix_prob:
                fixed_bugs.append(severity)
            else:
                bugs[i] = (fix_prob * failure_factor, severity)
                hours_left -= 1
    return fixed_bugs

def get_expected_total_severity(fixed_bugs):
    return sum(fixed_bugs)

def main():
    bugs_file = "bugs.txt"
    bugs_count, hours_left, failure_factor, bugs = get_bugs_info(bugs_file)
    fixed_bugs = get_fixed_bugs(bugs_count, hours_left, failure_factor, bugs)
    expected_total_severity = get_expected_total_severity(fixed_bugs)
    print(expected_total_severity)

if __name__ == '__main__':
    main()

