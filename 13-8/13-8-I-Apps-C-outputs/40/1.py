
def get_available_space(apps):
    total_space = 0
    for app in apps:
        total_space += app[1]
    return total_space

def get_max_apps(apps, available_space):
    max_apps = 0
    selected_apps = []
    for app in apps:
        if app[0] <= available_space:
            max_apps += 1
            selected_apps.append(app[2])
            available_space -= app[0]
    return max_apps, selected_apps

def main():
    n, c = map(int, input().split())
    apps = []
    for i in range(n):
        d, s = map(int, input().split())
        apps.append((d, s, i+1))
    max_apps, selected_apps = get_max_apps(apps, c)
    print(max_apps)
    print(*selected_apps)

if __name__ == '__main__':
    main()

