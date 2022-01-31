what_i_have = []
f = open("output.txt", "r")
for x in f:
    print(x)
    what_i_have.append(x)

print(what_i_have)


codes = []
values = []
for i in range(len(what_i_have)):
    one_line = what_i_have[i]
    one_line = one_line.replace("\n", "")
    a = one_line.split("|")
    codes.append(a[0])
    values.append(a[1])

print(codes)
print(values)

yes = []
no = []

for z in range(len(codes)):
    temp_code = codes[z]
    if values[z] == "1":
        # code is true
        for x in range(len(temp_code) - 1):
            try_key = temp_code[x] + temp_code[x + 1]
            if not try_key in yes:
                yes.append(try_key)
    else:
        for x in range(len(temp_code) - 1):
            try_key = temp_code[x] + temp_code[x + 1]
            if not try_key in yes:
                no.append(try_key)

print(yes)
print(no)

ihope = []

for d in range(len(yes)):
    if not yes[d] in no:
        ihope.append(yes[d])


print("{} are possible keys".format(ihope))
