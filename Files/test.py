import os
import string

path=os.getcwd()
print(path)
x=path.rfind("\\")

path=path[:x]
print(path)
