
def get_mentors(skills, quarrels):
    mentors = [0] * len(skills)
    for i in range(len(skills)):
        for j in range(i+1, len(skills)):
            if skills[i] > skills[j] and (i, j) not in quarrels and (j, i) not in quarrels:
                mentors[i] += 1
                mentors[j] += 1
    return mentors

def main():
    n, k = map(int, input().split())
    skills = list(map(int, input().split()))
    quarrels = set()
    for _ in range(k):
        x, y = map(int, input().split())
        quarrels.add((x, y))
        quarrels.add((y, x))
    mentors = get_mentors(skills, quarrels)
    print(*mentors, sep='\n')

if __name__ == '__main__':
    main()

