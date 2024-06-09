
import sys
input = sys.stdin.read()
n, k = map(int, input.split('\n')[0].split())
courses = [tuple(map(int, input.split('\n')[i].split())) for i in range(1, n+1)]

def f1(courses, k):
    # write your code here
    return 0

def f2(courses, k):
    # write your code here
    return 0

if __name__ == '__main__':
    print(f1(courses, k))
    print(f2(courses, k))

