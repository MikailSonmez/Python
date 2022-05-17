# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(c)        # [1,2,3,4,5,6]
# print(c[:5])    # [1,2,3,4,5]

# stuff = list()
# stuff.append("book")
# stuff.append(99)
# print(stuff)       # ["book", 99]

# stuff.append("cookie")
# print(stuff)       # ["book", 99, "cookie"]

# c = [1,4,5,6,8,45]
# if 6 in c:
#     print("True")
# if 20 not in c:
#     print("True")
# else:
#     print("Wrong")

# friends = ["Joseph", "Glen", "Sally"]
# friends.sort()
# print(friends)

# nums = [3, 32,34,12,67,115, 75]
# print(len(nums))
# print(max(nums))
# print(min(nums))
# print(sum(nums))
# print(sum(nums)/len(nums))

# total = 0
# count = 0
# while True:
#     inp = input("Enter a number: ")
#     if inp == "done" : break
#     value = float(inp)
#     total = total + value
#     count = count + 1
# average = total/count
# print("Average", average)

numlist = list()
while True:
     inp = input("Enter a number: ")
     if inp == "done" : break
     value = float(inp)
     numlist.append(value)
average = sum(numlist) / len(numlist)
print("Average", average)