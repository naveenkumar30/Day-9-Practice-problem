def find_five_digit():
    a=0
    b=0
    c=0
    d=0
    for i in range(9,-1,-1):
        a=int(i-2)
        b=int(a-2)
        c=int(b-2)
        d=int(b)
        if(b+c+d==i and a+b+c+d+i==19):
            break
    s=str(i)+str(a)+str(b)+str(c)+str(d)
    print(s)

find_five_digit()def find_five_digit():
    a=0
    b=0
    c=0
    d=0
    for i in range(9,-1,-1):
        a=int(i-2)
        b=int(a-2)
        c=int(b-2)
        d=int(b)
        if(b+c+d==i and a+b+c+d+i==19):
            break
    s=str(i)+str(a)+str(b)+str(c)+str(d)
    print(s)

find_five_digit()
