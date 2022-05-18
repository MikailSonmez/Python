#  Tuples use normal bracket and immutable

# x = ('glen', 'sally', "joseph")
# print(x)
# print(x[1])

# y = (1,7,5)
# print(y)
# print(max(y))
# dont accept y[1] = 8

# l=list()
# print(dir(l))
# t=tuple()
# print(dir(t))

# (x, y) = (4, 'fred')
# print(x)
# print(x,y)

# d = dict()
# d['csev'] = 2
# d['cwen'] = 4
# for (k,v) in d.items():
#  print(k,v)

# tups = d.items()
# print(tups)

# Tuples are Comparable
(0, 1, 2) < (5, 1, 2)                   #true
(0, 1, 2000) < (0, 3, 4)                #true
('Jones', 'Sally') < ('Jones', 'Sam')   #true
# ('Jones', 'Sally') = ('Adams', 'Sam')   #true