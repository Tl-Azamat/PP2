import os
f  = r"C:\Users\Azamat2005\Desktop\Python\Prob\pp2\week5"

if os.path.exists(f):
    if os.path.isdir(f):
        print(os.path.dirname(f))
    else:
        print(os.path.basename(f))