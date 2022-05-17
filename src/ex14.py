s = "monty pyhton"

# print(s[0:4])
# print(s[6:7])
# print(s[6:20])
#
# print(s[:2])
# print(s[8:])
# print(s[:])
# print(s)

# a = "Hello"
# b = a + "there"
# print(b)
# c = a + " " + "There"
# print(c)

# if "m" in "banana":
#    print("Found it")
# else:
#    print(None)

# print(s.lower())
# print(s.upper())
# print(type(s))
# print(dir(s))

# fruit ="banana"
# pos = fruit.find("na")
# print(pos)
# aa = fruit.find("z")
# print(aa)

# greet = "Hello Bob"
# nstr = greet.replace("Bob", "Jane")
# print(nstr)
# str = greet.replace("o", "x")
# print(str)

# greet = " Hello Bob "
# print(greet.lstrip())
# print(greet.rstrip())
# print(greet.strip())

# line = "Please have a nice day"
# if line.startswith("Please"):
#    print("YES")
# if line.startswith("P"):
#    print("NOPE")

data="from step.marq@itu.edu.tr Sat June 3 09:24:45 2020"
atpos = data.find("@")
print(atpos)
sppos = data.find(" ", atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)