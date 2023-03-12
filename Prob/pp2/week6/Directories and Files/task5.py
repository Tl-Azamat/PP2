mylist = ['Rustem ', 'Temirgali ', 'Ruslanuly ', 'Aslan ', "Temirgali ", 'Ersultan ', 'Temirgali']

with open(r"C:\Users\Azamat2005\Desktop\Python\Prob\pp2\week5", 'w') as file:
    for x in mylist:
        file.write(x)

f = open(r"C:\Users\Azamat2005\Desktop\Python\Prob\pp2\week5")
print(f.read())