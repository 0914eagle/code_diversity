
def get_target_value(section_size, operator, target):
    if operator == '-':
        return section_size - target
    elif operator == '*':
        return section_size * target
    else:
        return target

def is_valid_assignment(section_size, operator, target, assignment):
    if len(assignment) != section_size:
        return False
    
    if operator == '-':
        if assignment[0] - assignment[-1] != target:
            return False
    elif operator == '*':
        if assignment[0] * assignment[-1] != target:
            return False
    else:
        if assignment[0] + assignment[-1] != target:
            return False
    
    for i in range(1, section_size):
        if assignment[i] <= assignment[i-1]:
            return False
    
    return True

def count_valid_assignments(section_size, operator, target):
    num_valid_assignments = 0
    for assignment in itertools.permutations(range(1, section_size+1)):
        if is_valid_assignment(section_size, operator, target, assignment):
            num_valid_assignments += 1
    
    return num_valid_assignments

def main():
    n, m, t, op = map(int, input().split())
    print(count_valid_assignments(m, op, t))

if __name__ == '__main__':
    main()

