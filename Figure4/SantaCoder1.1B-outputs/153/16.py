def Strongest_Extension(class_name, extensions):
    
    # Your code here
    return class_name + "." + max(extensions, key=len)

# Example
class_name = "Slices"
extensions = ['SErviNGSliCes', 'Cheese', 'StuFfed']
print(Strongest_Extension(class_name, extensions))

# 2.3.3
