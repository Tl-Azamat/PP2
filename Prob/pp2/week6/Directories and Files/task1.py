import os
for root, directories, files in os.walk(r"C:\Users\Azamat2005\Desktop\Python\Prob\pp2\week5"):
    print(root)
    for directory in directories:
        print(directory)
    for file in files:
        print(file)