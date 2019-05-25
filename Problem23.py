#PF-Prac-23
def divisible_by_sum(number):
    #start writing your code here
    temp=number
    s=0
    while(number>0):
        r=number%10
        number=number//10
        s=s+r
    if(temp%s==0):
        return True
    else:
        return False

    
number=66
print(divisible_by_sum(number))
