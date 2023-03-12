import os
print('Exist:', os.access(r"C:\Users\Azamat2005\Desktop\Python\Prob\pp2\week5", os.F_OK))
print('Readable:', os.access(r"C:\Users\Azamat2005\Desktop\Python\Prob\pp2\week5", os.R_OK))
print('Writable:', os.access(r"C:\Users\Azamat2005\Desktop\Python\Prob\pp2\week5", os.W_OK))
print('Executable:', os.access(r"C:\Users\Azamat2005\Desktop\Python\Prob\pp2\week5", os.X_OK))