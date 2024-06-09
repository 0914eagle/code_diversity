
def is_good_lab(lab):
    n = len(lab)
    for i in range(n):
        for j in range(n):
            if lab[i][j] != 1 and not can_form_sum(lab[i][j], lab[i], lab[j]):
                return False
    return True

def can_form_sum(target, row, col):
    for i in range(len(row)):
        for j in range(len(col)):
            if row[i] + col[j] == target:
                return True
    return False

if __name__ == '__main__':
    n = int(input())
    lab = []
    for i in range(n):
        lab.append(list(map(int, input().split())))
    print("Yes") if is_good_lab(lab) else print("No")

