#PF-Prac-7
def seed_no(number,ref_no):
    t=number
    while(number!=0):
        r=number%10
        t=t*r
        number=number//10
    if(t==ref_no):
        return True
    else:
        return False



number=45
ref_no=1000
print(seed_no(number,ref_no))
