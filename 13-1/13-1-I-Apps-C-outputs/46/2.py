
def f1(n, c):
    # find the largest app that can be installed
    largest_app = 0
    for i in range(n):
        if d[i] <= c:
            largest_app = max(largest_app, s[i])
    
    # find the largest number of apps that can be installed
    max_apps = 0
    for i in range(n):
        if s[i] <= largest_app:
            max_apps += 1
    
    return max_apps

def f2(n, c):
    # sort the apps by their storage size in descending order
    sorted_apps = sorted(range(n), key=lambda i: s[i], reverse=True)
    
    # install the apps in the sorted order
    installed_apps = []
    for i in sorted_apps:
        if s[i] <= c:
            installed_apps.append(i)
            c -= s[i]
    
    return installed_apps

if __name__ == '__main__':
    n, c = map(int, input().split())
    d = list(map(int, input().split()))
    s = list(map(int, input().split()))
    print(f1(n, c))
    print(*f2(n, c))

