
def get_max_apps(n, c, apps):
    # Sort the apps by their storage size in descending order
    apps.sort(key=lambda x: x[1], reverse=True)
    # Initialize the number of apps installed as 0
    num_apps = 0
    # Initialize the total disk space used as 0
    total_disk_space = 0
    # Loop through the apps
    for app in apps:
        # Check if the app can be installed
        if total_disk_space + app[0] <= c:
            # Increment the number of apps installed
            num_apps += 1
            # Increment the total disk space used
            total_disk_space += app[1]
    # Return the maximum number of apps that can be installed
    return num_apps

def get_app_order(n, c, apps):
    # Sort the apps by their storage size in descending order
    apps.sort(key=lambda x: x[1], reverse=True)
    # Initialize the number of apps installed as 0
    num_apps = 0
    # Initialize the total disk space used as 0
    total_disk_space = 0
    # Initialize the app order as an empty list
    app_order = []
    # Loop through the apps
    for app in apps:
        # Check if the app can be installed
        if total_disk_space + app[0] <= c:
            # Increment the number of apps installed
            num_apps += 1
            # Increment the total disk space used
            total_disk_space += app[1]
            # Add the app to the app order
            app_order.append(app[2])
    # Return the app order
    return app_order

if __name__ == '__main__':
    n, c = map(int, input().split())
    apps = []
    for i in range(n):
        d, s = map(int, input().split())
        apps.append([d, s, i+1])
    print(get_max_apps(n, c, apps))
    print(*get_app_order(n, c, apps))

