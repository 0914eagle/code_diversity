
def get_max_apps(n, c, apps):
    # Sort the apps by their download size in descending order
    apps.sort(key=lambda x: x[0], reverse=True)
    
    # Initialize the installed apps and the available disk space
    installed_apps = []
    available_space = c
    
    # Loop through the apps and install them if there is enough space
    for app in apps:
        if available_space >= app[0]:
            installed_apps.append(app)
            available_space -= app[0]
    
    # Return the maximum number of apps that can be installed
    return len(installed_apps)

def get_installation_order(n, c, apps):
    # Sort the apps by their download size in descending order
    apps.sort(key=lambda x: x[0], reverse=True)
    
    # Initialize the installed apps and the available disk space
    installed_apps = []
    available_space = c
    
    # Loop through the apps and install them if there is enough space
    for app in apps:
        if available_space >= app[0]:
            installed_apps.append(app)
            available_space -= app[0]
    
    # Return the installation order of the apps
    return [app[1] for app in installed_apps]

if __name__ == '__main__':
    n, c = map(int, input().split())
    apps = []
    for _ in range(n):
        d, s = map(int, input().split())
        apps.append((d, s))
    print(get_max_apps(n, c, apps))
    print(' '.join(str(app) for app in get_installation_order(n, c, apps)))

