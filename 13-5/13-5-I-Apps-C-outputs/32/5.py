
def f1(n, m, s, a, b, c):
    # sort the bugs by complexity in descending order
    a.sort(reverse=True)
    # sort the students by their ability level in descending order
    b.sort(reverse=True)
    # initialize the number of passes given to each student to 0
    passes = [0] * n
    # initialize the number of days needed to fix all bugs to 0
    days = 0
    # loop through each bug and try to assign it to a student
    for i in range(m):
        # find the student with the highest ability level who can fix the current bug
        for j in range(n):
            if b[j] >= a[i]:
                # give the student one pass for their help
                passes[j] += 1
                # increment the number of days needed to fix all bugs
                days += 1
                break
        # if the university has reached the maximum number of passes, return "NO"
        if sum(passes) > s:
            return "NO"
    # if the university has fixed all bugs, return "YES" and the schedule of work
    return "YES\n" + " ".join(str(i + 1) for i in range(m) if passes[i] > 0)

def f2(...):
    # implement f2 here
    pass

if __name__ == '__main__':
    n, m, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    print(f1(n, m, s, a, b, c))

