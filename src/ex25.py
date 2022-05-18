# d = {'a':10, 'b':1, 'c':22 }
# d.items()
# # dict_items([('a', 10), ('c', 22), ('b', 1)])

# t = sorted(d.items())
# print(t)               #[('a', 10), ('b', 1), ('c', 22)]
# for k, v in t:
#     print(k, v)

# tmp = list()
# for k, v in d.items():
#    tmp.append((v, k))
# print(tmp)    # [(10, 'a'), (1, 'b'), (22, 'c')]
# tmp = sorted(tmp, reverse = True)
# print(tmp)

fhand = open('ex_17.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse = True)
for val, key in lst[:10]:
    print(key, val)

# or
c = {'a':10, 'b':1, 'c':22 }
print( sorted( [ (v,k) for k,v in c.items() ] ) )