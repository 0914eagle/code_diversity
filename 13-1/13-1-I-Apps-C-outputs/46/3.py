
def f1(n, c):
    # initialize the available disk space and the list of apps
    available_space = c
    apps = []
    
    # loop through the input and add the apps to the list
    for i in range(n):
        d, s = map(int, input().split())
        apps.append((d, s))
    
    # sort the apps in descending order by their download size
    apps.sort(key=lambda x: x[0], reverse=True)
    
    # initialize the number of apps that can be installed
    num_apps = 0
    
    # loop through the apps and install them if there is enough space
    for d, s in apps:
        if available_space >= d:
            num_apps += 1
            available_space -= d
        else:
            break
    
    # return the number of apps that can be installed
    return num_apps

def f2(n, c):
    # initialize the available disk space and the list of apps
    available_space = c
    apps = []
    
    # loop through the input and add the apps to the list
    for i in range(n):
        d, s = map(int, input().split())
        apps.append((d, s))
    
    # sort the apps in descending order by their download size
    apps.sort(key=lambda x: x[0], reverse=True)
    
    # initialize the number of apps that can be installed
    num_apps = 0
    
    # loop through the apps and install them if there is enough space
    for d, s in apps:
        if available_space >= d:
            num_apps += 1
            available_space -= d
        else:
            break
    
    # return the list of apps that can be installed, in the order they should be installed
    return [i+1 for i in range(num_apps)]

if __name__ == '__main__':
    n, c = map(int, input().split())
    print(f1(n, c))
    print(*f2(n, c))

