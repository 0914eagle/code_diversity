
def get_input():
    R, B = map(int, input().split())
    rebels = []
    for i in range(R):
        x, y = map(int, input().split())
        rebels.append((x, y))
    bases = []
    for i in range(B):
        x, y = map(int, input().split())
        bases.append((x, y))
    return R, B, rebels, bases

def check_intersection(rebels, bases):
    for i in range(len(rebels)):
        for j in range(len(bases)):
            if i != j and (rebels[i][0] == bases[j][0] and rebels[i][1] == bases[j][1]):
                return False
    return True

def solve(R, B, rebels, bases):
    if check_intersection(rebels, bases):
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    R, B, rebels, bases = get_input()
    print(solve(R, B, rebels, bases))

