
def get_max_apps(n, c, apps):
    # Sort the apps by their storage size in descending order
    apps.sort(key=lambda x: x[1], reverse=True)
    # Initialize the number of apps installed to 0
    num_apps = 0
    # Initialize the total disk space used to 0
    total_disk_space = 0
    # Loop through the apps
    for app in apps:
        # Check if the app can be installed
        if total_disk_space + app[0] <= c:
            # If the app can be installed, increment the number of apps installed
            num_apps += 1
            # Add the app's download size to the total disk space used
            total_disk_space += app[0]
    # Return the number of apps that can be installed
    return num_apps

def get_app_order(n, c, apps):
    # Sort the apps by their storage size in descending order
    apps.sort(key=lambda x: x[1], reverse=True)
    # Initialize the number of apps installed to 0
    num_apps = 0
    # Initialize the total disk space used to 0
    total_disk_space = 0
    # Initialize the app order list
    app_order = []
    # Loop through the apps
    for app in apps:
        # Check if the app can be installed
        if total_disk_space + app[0] <= c:
            # If the app can be installed, add it to the app order list
            app_order.append(app[2])
            # Increment the number of apps installed
            num_apps += 1
            # Add the app's download size to the total disk space used
            total_disk_space += app[0]
    # Return the app order list
    return app_order

if __name__ == '__main__':
    # Read the input
    n, c = map(int, input().split())
    apps = []
    for i in range(n):
        d, s = map(int, input().split())
        apps.append([d, s, i+1])
    # Call the functions
    num_apps = get_max_apps(n, c, apps)
    app_order = get_app_order(n, c, apps)
    # Print the output
    print(num_apps)
    print(*app_order)

