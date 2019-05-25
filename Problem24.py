#PF-Prac-24
def find_gcd(num1,num2):
    #start writing your code here
    if(num2==0):
        return num1
    else:
        return find_gcd(num2,num1%num2)
    

num1=14
num2=35
print(find_gcd(num1,num2))
