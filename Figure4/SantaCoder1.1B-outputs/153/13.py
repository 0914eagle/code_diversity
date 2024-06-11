def Strongest_Extension(class_name, extensions):
    
    # Write your code here.
    return class_name + "." + max(extensions, key=len)

