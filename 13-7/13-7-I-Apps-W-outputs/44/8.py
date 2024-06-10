
def get_max_fragment_area(glass_fragments):
    return max(glass_fragments, key=lambda x: x[0] * x[1])[0] * max(glass_fragments, key=lambda x: x[0] * x[1])[1]

def carve_glass(glass_sheet, cuts):
    glass_fragments = [(glass_sheet[1], glass_sheet[0])]
    for cut in cuts:
        if cut[0] == "H":
            y = cut[1]
            for i in range(len(glass_fragments)):
                if glass_fragments[i][1] > y:
                    glass_fragments.insert(i, (glass_fragments[i][0], y))
                    break
                elif i == len(glass_fragments) - 1:
                    glass_fragments.append((glass_fragments[i][0], y))
                    break
        else:
            x = cut[1]
            for i in range(len(glass_fragments)):
                if glass_fragments[i][0] > x:
                    glass_fragments.insert(i, (x, glass_fragments[i][1]))
                    break
                elif i == len(glass_fragments) - 1:
                    glass_fragments.append((x, glass_fragments[i][1]))
                    break
        print(get_max_fragment_area(glass_fragments))

def main():
    glass_sheet = list(map(int, input().split()))
    n = int(input())
    cuts = []
    for i in range(n):
        cut = input().split()
        cuts.append(cut)
    carve_glass(glass_sheet, cuts)

if __name__ == '__main__':
    main()

