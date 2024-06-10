
def get_max_prettiness(prettinesses):
    prettinesses.sort(reverse=True)
    max_prettiness = 0
    for i in range(len(prettinesses)):
        for j in range(i+1, len(prettinesses)):
            if prettinesses[i] % prettinesses[j] == 0:
                continue
            for k in range(j+1, len(prettinesses)):
                if prettinesses[j] % prettinesses[k] == 0:
                    continue
                if prettinesses[i] + prettinesses[j] + prettinesses[k] > max_prettiness:
                    max_prettiness = prettinesses[i] + prettinesses[j] + prettinesses[k]
    return max_prettiness

def main():
    queries = int(input())
    for _ in range(queries):
        n = int(input())
        prettinesses = list(map(int, input().split()))
        print(get_max_prettiness(prettinesses))

if __name__ == '__main__':
    main()

