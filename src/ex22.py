counts = dict()
names = ["csev", "cwen", "csev", "zqian", "cwen"]
# for nm in names:
#     if nm not in counts:
#         counts[nm] = 1
#     else:
#         counts[nm] = counts[nm] + 1
# print(counts)      #{'csev': 2, 'cwen': 2, 'zqian': 1}
#
# get()

for nm in names:
    counts[nm] = counts.get(nm, 0) + 1
print(counts)        #{'csev': 2, 'cwen': 2, 'zqian': 1}

# ex

couts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(couts.get('mrugesh', 0))    #42