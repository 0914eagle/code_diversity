
def get_apps_to_install(n, c, apps):
    # Sort the apps by their download size in descending order
    apps.sort(key=lambda x: x[0], reverse=True)
    # Initialize variables to keep track of the available disk space and the number of installed apps
    available_space = c
    installed_apps = 0
    # Initialize a list to store the ordered list of apps to install
    ordered_apps = []
    # Loop through the apps and install them if there is enough space
    for app in apps:
        if available_space >= app[0]:
            ordered_apps.append(app[1])
            available_space -= app[0]
            installed_apps += 1
    # Return the number of installed apps and the ordered list of apps
    return installed_apps, ordered_apps

def main():
    # Read the input data
    n, c = map(int, input().split())
    apps = []
    for _ in range(n):
        d, s = map(int, input().split())
        apps.append((d, s))
    # Call the function to get the apps to install
    installed_apps, ordered_apps = get_apps_to_install(n, c, apps)
    # Print the output
    print(installed_apps)
    print(" ".join(map(str, ordered_apps)))

if __name__ == '__main__':
    main()

