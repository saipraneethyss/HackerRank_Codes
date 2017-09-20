import builtins
    n = int(input())
    integer_list = map(int, input().split())
    print(builtins.hash(tuple(integer_list)))