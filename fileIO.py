import os

fname = 'Hello.exe'

fpath = 'C:\\Users\\Mohamed\\Desktop\\A\\'

abPath = os.path.join(fpath,fname)
print(abPath)
listPath= os.listdir(fpath)
print(listPath)
timePath=os.path.getmtime(fpath)
print(timePath)

for file in os.listdir(fpath):
    if file.endswith(".txt"):
        print(os.path.join(fpath, file))
        timePath=os.path.getmtime(fpath)
        print(timePath)
