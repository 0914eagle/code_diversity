
def get_max_apps(n, c, apps):
    # Sort the apps by their storage size in descending order
    apps.sort(key=lambda x: x[1], reverse=True)
    # Initialize the number of apps installed to 0
    num_apps = 0
    # Initialize the total storage used to 0
    total_storage = 0
    # Initialize the list of apps to install
    app_list = []
    # Loop through the apps
    for app in apps:
        # Check if the app can be installed
        if app[0] + total_storage <= c:
            # Add the app to the list of apps to install
            app_list.append(app[2])
            # Increment the number of apps installed
            num_apps += 1
            # Increment the total storage used
            total_storage += app[1]
    # Return the number of apps installed and the list of apps in the order they should be installed
    return num_apps, app_list

def main():
    # Read the input
    n, c = map(int, input().split())
    apps = []
    for i in range(n):
        d, s = map(int, input().split())
        apps.append([d, s, i+1])
    # Call the function to get the maximum number of apps that can be installed
    num_apps, app_list = get_max_apps(n, c, apps)
    # Print the number of apps installed
    print(num_apps)
    # Print the list of apps in the order they should be installed
    print(*app_list)

if __name__ == '__main__':
    main()

