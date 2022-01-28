# JayaShankar's Sort Function
n = open("output1.txt","r") # open file, read only
s = open("sortOutput01.txt","w") # open file, write
lines = n.readlines()
lines.sort()
for line in lines:
    s.write(line)
n.close()
s.close()