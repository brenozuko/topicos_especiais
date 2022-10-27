import os

dir = os.path.join(os.sep, 'c:\\', 'temp')

if (not os.path.exists(dir)):
    os.makedirs(dir)

os.chdir(dir)

# for i in range(1,6):
#     os.mkdir(str(i))


# for i in os.listdir(dir):
#     atual = os.path.join(os.sep, os.getcwd(), i)
#     novo = os.path.join(os.sep, os.getcwd(), "dir_%s" % i)
#     print(atual, novo)
#     os.rename(atual, novo)


for i in os.listdir(dir):
    os.rmdir(str(i))
    