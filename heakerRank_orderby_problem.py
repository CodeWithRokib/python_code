# Collections.OrderedDict() in Python - Hacker Rank Solution
# Python 3
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Collections.OrderedDict() in Python - Hacker Rank Solution START

from collections import*;
N = int(input());
d = OrderedDict();
for i in range(N):
    item = input().split()
    itemPrice = int(item[-1])
    itemName = " ".join(item[:-1])
    if(d.get(itemName)):
        d[itemName] += itemPrice
    else:
        d[itemName] = itemPrice
for i in d.keys():
    print(i, d[i])
