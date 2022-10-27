import os
dir = os.path.join(os.sep, 'c:\\', 'temp')

if(not os.path.exists(dir)):
    os.makedirs(dir)


os.chdir(dir)
for i in range(1,6):
    os.mkdir(str(i))

