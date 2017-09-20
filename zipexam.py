stud = []
for k in range(int((input().split())[1])):
    stud.append(list(map(float,input().split())))
print(*[sum(list(i))/(k+1) for i in zip(*stud)],sep="\n")