def Strongest_Extension(class_name, extensions):
    
    # Your code here
    return class_name + '.' + max(extensions, key=len)

# Test