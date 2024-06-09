
def is_good_lab(lab):
    n = len(lab)
    for i in range(n):
        for j in range(n):
            if lab[i][j] != 1 and not can_be_formed(lab, i, j):
                return False
    return True

def can_be_formed(lab, i, j):
    n = len(lab)
    for k in range(n):
        if lab[i][k] + lab[k][j] == lab[i][j]:
            return True
    return False

if __name__ == '__main__':
    n = int(input())
    lab = []
    for i in range(n):
        lab.append(list(map(int, input().split())))
    print("Yes") if is_good_lab(lab) else print("No")

