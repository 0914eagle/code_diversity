def Strongest_Extension(class_name, extensions):
    
    # Your code here
    return class_name + '.' + max(extensions, key=len)


# In[13]:


class_name = 'Slices'
extensions = ['SErviNGSliCes', 'Cheese', 'StuFfed']
print(Strongest_Extension(class_name, extensions))


#