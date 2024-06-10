
def get_apps_to_install(n, c, apps):
    # Sort the apps by their download size in descending order
    apps.sort(key=lambda x: x[0], reverse=True)
    
    # Initialize variables to keep track of the apps that can be installed and the total disk space used
    installed_apps = []
    total_disk_space = 0
    
    # Iterate through the apps and add them to the list of installed apps if there is enough disk space
    for app in apps:
        if total_disk_space + app[0] <= c:
            installed_apps.append(app[1])
            total_disk_space += app[0]
    
    return installed_apps

def get_installation_order(n, c, apps):
    # Get the list of apps that can be installed
    installed_apps = get_apps_to_install(n, c, apps)
    
    # Sort the apps by their storage size in descending order
    installed_apps.sort(key=lambda x: x[1], reverse=True)
    
    # Return the list of apps in the order that they should be installed
    return installed_apps

if __name__ == '__main__':
    n, c = map(int, input().split())
    apps = []
    for _ in range(n):
        d, s = map(int, input().split())
        apps.append((d, s))
    print(len(get_installation_order(n, c, apps)))
    for app in get_installation_order(n, c, apps):
        print(app)

