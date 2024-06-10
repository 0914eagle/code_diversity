
def is_possible(projects, rating):
    if len(projects) == 0:
        return True
    if rating < projects[0][0]:
        return False
    return is_possible(projects[1:], rating + projects[0][1])

def main():
    n, r = map(int, input().split())
    projects = []
    for i in range(n):
        a, b = map(int, input().split())
        projects.append((a, b))
    if is_possible(projects, r):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

