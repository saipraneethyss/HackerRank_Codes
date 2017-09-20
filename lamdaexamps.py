from collections import Counter as cn
st = sorted(cn(input()).items(),key= lambda x: (-x[1],x[0]))[:3]
print("\n".join(s[0]+" "+str(s[1]) for s in st))

(n,m) = map(int,input().split())
(data,k) = ([list(map(int,input().split())) for _ in range(n)],int(input().rstrip()))
print(*[" ".join(map(str,i)) for i in sorted(data,key = lambda x:x[k])],sep='\n')