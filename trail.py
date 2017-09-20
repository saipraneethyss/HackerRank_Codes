def wrap(string, max_width):
    return textwrap.fill(string,max_width)

    s = input()
    print(any(i.isalnum() for i in s))
    print(any(i.isalpha() for i in s))
    print(any(i.isdigit() for i in s))
    print(any(i.islower() for i in s))
    print(any(i.isupper() for i in s))

    def sqgen(n):
    a = (n/4)+1;b = (n/4)-1
    if(a**2-b**2)==n:
        return n
    else:
        return None
k = int(input())
tiles = [i for i in range(4,k+1) if i%4==0]
print(tiles)
n1 = [sqgen(i) for i in tiles]
print(len(n1))