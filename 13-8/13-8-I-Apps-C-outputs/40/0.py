
def get_app_order(n, c, apps):
    # Sort the apps by their download size in descending order
    apps.sort(key=lambda x: x[0], reverse=True)
    
    # Initialize the installed apps and their sizes
    installed_apps = []
    installed_size = 0
    
    # Loop through the apps and install them if there is enough space
    for app in apps:
        if installed_size + app[0] <= c:
            installed_apps.append(app[1])
            installed_size += app[0]
    
    return installed_apps

def get_max_apps(n, c, apps):
    # Get the order of the apps to install
    app_order = get_app_order(n, c, apps)
    
    # Count the number of apps that can be installed
    max_apps = 0
    for app in app_order:
        if app[0] <= c:
            max_apps += 1
    
    return max_apps

if __name__ == '__main__':
    n, c = map(int, input().split())
    apps = []
    for i in range(n):
        d, s = map(int, input().split())
        apps.append([d, s])
    print(get_max_apps(n, c, apps))
    print(*get_app_order(n, c, apps), sep=' ')

