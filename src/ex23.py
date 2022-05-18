# counts = dict()
# print('Enter a line of text:')
# line = input('')
#
# words = line.split()
#
# print('Words:', words)
#
# print('Counting...')
# for word in words:
#     counts[word] = counts.get(word, 0) + 1
# print('Counts', counts)

# counts = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
# for key in counts:             # key or kee or hey doesnt matter
#    print(key, counts[key])

# jjj = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
# print(list(jjj))
# print(jjj.keys())
# print(jjj.values())
# print(jjj.items())
# for aaa,bbb in jjj.items():
#    print(aaa,bbb)

name = input('Enter file:')
handle = open(name)
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword,  bigcount)