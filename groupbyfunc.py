from itertools import groupby
astring = input()
l = []
for i,k in groupby(astring):
    l.append((len(list(k)),int(i)))
print(*l,sep=' ')