
def is_good_lab(lab):
    n = len(lab)
    for i in range(n):
        for j in range(n):
            if lab[i][j] != 1 and not any(lab[i][k] + lab[k][j] == lab[i][j] for k in range(n)):
                return False
    return True

def main():
    n = int(input())
    lab = []
    for i in range(n):
        lab.append([int(x) for x in input().split()])
    print("Yes") if is_good_lab(lab) else print("No")

if __name__ == '__main__':
    main()

