
def f1(n, c):
    # Initialize a list to store the apps
    apps = []
    # Iterate through the input and add the apps to the list
    for i in range(n):
        d, s = map(int, input().split())
        apps.append((d, s))
    # Sort the apps in descending order of their download size
    apps.sort(key=lambda x: x[0], reverse=True)
    # Initialize a variable to store the total disk space used
    total_disk_space = 0
    # Initialize a list to store the apps that can be installed
    installable_apps = []
    # Iterate through the apps and check if they can be installed
    for app in apps:
        if total_disk_space + app[0] <= c:
            installable_apps.append(app)
            total_disk_space += app[0]
    # Return the maximum number of apps that can be installed
    return len(installable_apps)

def f2(n, c):
    # Initialize a list to store the apps
    apps = []
    # Iterate through the input and add the apps to the list
    for i in range(n):
        d, s = map(int, input().split())
        apps.append((d, s))
    # Sort the apps in descending order of their download size
    apps.sort(key=lambda x: x[0], reverse=True)
    # Initialize a variable to store the total disk space used
    total_disk_space = 0
    # Initialize a list to store the apps that can be installed
    installable_apps = []
    # Iterate through the apps and check if they can be installed
    for app in apps:
        if total_disk_space + app[0] <= c:
            installable_apps.append(app)
            total_disk_space += app[0]
    # Return the list of installable apps in the order they should be installed
    return [str(i+1) for i in range(len(installable_apps))]

if __name__ == '__main__':
    n, c = map(int, input().split())
    print(f1(n, c))
    print(" ".join(f2(n, c)))

