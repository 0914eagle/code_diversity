
def read_input():
    n = int(input())
    vertical_spec = []
    for i in range(n):
        line = input().split()
        if line[0] == '0':
            vertical_spec.append([])
        else:
            vertical_spec.append([int(x) for x in line])
    horizontal_spec = []
    for i in range(n):
        line = input().split()
        if line[0] == '0':
            horizontal_spec.append([])
        else:
            horizontal_spec.append([int(x) for x in line])
    return n, vertical_spec, horizontal_spec

def is_valid_marking(marking, vertical_spec, horizontal_spec):
    for i in range(len(vertical_spec)):
        for j in range(len(vertical_spec[i])):
            if marking[i][j] == 1 and marking[i][j+1] == 1:
                return False
    for i in range(len(horizontal_spec)):
        for j in range(len(horizontal_spec[i])):
            if marking[j][i] == 1 and marking[j+1][i] == 1:
                return False
    return True

def generate_marking(n, vertical_spec, horizontal_spec):
    marking = [[0 for _ in range(n+1)] for _ in range(n)]
    for i in range(len(vertical_spec)):
        for j in range(len(vertical_spec[i])):
            marking[i][j] = 1
            marking[i][j+1] = 1
    for i in range(len(horizontal_spec)):
        for j in range(len(horizontal_spec[i])):
            marking[j][i] = 1
            marking[j+1][i] = 1
    return marking

def solve(n, vertical_spec, horizontal_spec):
    marking = generate_marking(n, vertical_spec, horizontal_spec)
    while not is_valid_marking(marking, vertical_spec, horizontal_spec):
        marking = generate_marking(n, vertical_spec, horizontal_spec)
    return marking

def main():
    n, vertical_spec, horizontal_spec = read_input()
    marking = solve(n, vertical_spec, horizontal_spec)
    for i in range(n):
        print(''.join([str(x) for x in marking[i]]))
    for i in range(n):
        print(''.join([str(x) for x in marking[i]]))

if __name__ == '__main__':
    main()

