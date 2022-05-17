# abc = "with three    words"
# stuff = abc.split()
# print(abc)
# print(stuff)
# print(len(stuff))
# print(range(len(stuff)))
# print(stuff[0])
#
# for w in stuff:
#    print(w)

# line = "aman;serhat;deve"
# thing = line.split(";")
# print(thing)

# fhand = open("ex_17.txt")
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith("From ") : continue
#   print(words[2])    # Sat
#     words = line.split()
#     email = words[1]
#     pieces = email.split("@")
#     print(pieces[1])

fhand = open("ex_17.txt")
for line in fhand:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 3 or wds[0] != "From" :
        continue
    print(wds[2])