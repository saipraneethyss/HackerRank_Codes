from itertools import product
a,b = map(int,input().split()),map(int,input().split())
print (*(product(a,b)))

from itertools import permutations as per
inp = input().split()
astring = list(inp[0])
astring.sort()
r = int(inp[1])
l = list(map(''.join,per(astring,r)))
print(*l,sep='\n')

#palindrome
(n,num) = (int(input()),list(input().split()))
print(all(int(i)>0 for i in num) and any(i[:]==i[::-1] for i in num))