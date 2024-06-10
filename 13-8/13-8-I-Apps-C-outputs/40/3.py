
def get_available_space(disk_space, apps):
    available_space = disk_space
    for app in apps:
        if app[0] > available_space:
            return 0
        available_space -= max(app[0], app[1])
    return available_space

def get_max_apps(disk_space, apps):
    max_apps = 0
    for i in range(len(apps)):
        if get_available_space(disk_space, apps[i:]) > 0:
            max_apps = i + 1
    return max_apps

def get_ordered_apps(disk_space, apps):
    ordered_apps = []
    for i in range(get_max_apps(disk_space, apps)):
        max_app = 0
        max_app_index = 0
        for j in range(len(apps)):
            if apps[j][0] + apps[j][1] > max_app and j not in ordered_apps:
                max_app = apps[j][0] + apps[j][1]
                max_app_index = j
        ordered_apps.append(max_app_index)
    return ordered_apps

def main():
    disk_space, n = map(int, input().split())
    apps = []
    for i in range(n):
        d, s = map(int, input().split())
        apps.append([d, s])
    print(get_max_apps(disk_space, apps))
    print(" ".join(map(str, get_ordered_apps(disk_space, apps))))

if __name__ == '__main__':
    main()

