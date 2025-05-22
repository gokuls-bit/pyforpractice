import os

# Set the path you want to list (use '.' for current directory)
directory_path = "/MSME"

# Check if path exists
contents =  os.listdir(directory_path)

print(contents)