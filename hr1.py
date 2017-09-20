if __name__ == '__main__':
    N = int(input())
    list_t = []
    for i in range(N):
        data = input().split()
        inp = [data[0]]+[int(data[i]) for i in range(1,len(data)) ]
        if(inp[0]=="insert"):
            list_t.insert(inp[1],inp[2])
        if(inp[0]=="remove"):
            list_t.remove(inp[1])
        if(inp[0]=="append"):
            list_t.append(inp[1])
        if(inp[0]=="sort"):
            list_t.sort()
        if(inp[0]=="pop"):
            list_t.pop()
        if(inp[0]=="reverse"):
            list_t.reverse()
        if(inp[0]=="print"):
            print(list_t)
        
        
