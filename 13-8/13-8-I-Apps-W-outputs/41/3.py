
def get_recorders(n, c, s, t, cn):
    recorders = []
    for i in range(n):
        recorder = None
        for j in range(len(recorders)):
            if recorders[j][0] <= s[i] < t[i] and recorders[j][1] == cn[i]:
                recorder = j
                break
        if recorder == None:
            recorders.append([s[i], cn[i]])
    return len(recorders)

def main():
    n, c = map(int, input().split())
    s = []
    t = []
    cn = []
    for i in range(n):
        si, ti, ci = map(int, input().split())
        s.append(si)
        t.append(ti)
        cn.append(ci)
    print(get_recorders(n, c, s, t, cn))

if __name__ == '__main__':
    main()

