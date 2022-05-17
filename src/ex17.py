# xfile = open("ex_17.txt")
# for chinese in xfile:
#    print(chinese)

# count = 0
# for line in xfile:
#     count = count + 1
# print("Line count: ", count)

# inp = xfile.read()
# print(len(inp))
# print(inp[:25])

# for line in xfile:
#    if line.startswith("chinese"):
#        print(line)

# for line in xfile:
#    line = line.rstrip()
#    if not line.startswith("chinese"):  #if not "@itu.edu.tr" in line:
#        continue
#    print(line)

fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened: ", fname)
    quit()

count = 0
for line in fhand:
    if line.startswith("chinese"):
        count = count + 1
print("there were", count, "chinese lines in", fname)