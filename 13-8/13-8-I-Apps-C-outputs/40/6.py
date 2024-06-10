
def get_max_apps(n, c, apps):
    # Sort the apps by download size in descending order
    apps.sort(key=lambda x: x[0], reverse=True)
    
    # Initialize variables
    installed_apps = 0
    total_size = 0
    
    # Loop through the apps and install them if there is enough space
    for app in apps:
        if total_size + app[0] <= c:
            total_size += app[0]
            installed_apps += 1
    
    return installed_apps

def get_installation_order(n, c, apps):
    # Initialize variables
    installed_apps = []
    total_size = 0
    
    # Loop through the apps and install them if there is enough space
    for app in apps:
        if total_size + app[0] <= c:
            total_size += app[0]
            installed_apps.append(app)
    
    # Sort the installed apps by download size in descending order
    installed_apps.sort(key=lambda x: x[0], reverse=True)
    
    return installed_apps

if __name__ == '__main__':
    n, c = map(int, input().split())
    apps = []
    for _ in range(n):
        d, s = map(int, input().split())
        apps.append((d, s))
    
    max_apps = get_max_apps(n, c, apps)
    print(max_apps)
    installation_order = get_installation_order(n, c, apps)
    print(*[app[1] for app in installation_order])

