from optparse import OptionGroup
import random
import string
import time

file = open("output.txt", "w")

repeat = 50
long = 10
# use = string.ascii_lowercase
use = "abcde"
output = []
outoutput = []
key = str(input("What is the key?"))

file.write("")

a = time.time()
for a in range(repeat):
    temp = ""
    for i in range(long):
        temp = temp + use[random.randint(0, len(use) - 1)]
    output.append(temp)


for s in range(len(output)):
    if key in output[s]:
        include = "1"
    else:
        include = "0"
    end = output[s] + "|" + include
    outoutput.append(end)
    file.write(end)
    file.write("\n")

print(output)
print(outoutput)
