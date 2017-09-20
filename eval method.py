n = int(input())
s = set(map(int, input().split())) 
for i in range(int(input())):
    eval('s.{0}({1})'.format(*input().split()+['']))

print(sum(s))

n = int(raw_input())
a = set(raw_input().split())
for i in range(int(input())):
    eval('a.{0}({1})'.format((raw_input().split())[0],set(raw_input().split())))
print(sum(list(map(int,a))))