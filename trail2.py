def print_formatted(number):
    num = len(str(bin(number).rsplit('b')[1]))
    for i in range(1,number+1):
        print(str(i).rjust(num)+' '+str(oct(i).rsplit('o')[1]).rjust(num)+' '+(str(hex(i).rsplit('x')[1]).rjust(num)).upper()+' '+str(bin(i).rsplit('b')[1]).rjust(num))
        
