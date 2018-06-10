import random

filename = input("input file name: ")

out = open(filename,"w")

for i in range(0,2000):
    x = random.randrange(0, 20000)
    y = random.randrange(0, 20000)
    out.writelines(str(x) + "," + str(y) + "\n")


out.close()