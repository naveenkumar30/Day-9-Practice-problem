#PF-Prac-13
import math
def close_number(num1,num2,num3):
    #start writing your code here
    if (math.fabs(num1-num2)==1 and math.fabs(num3-num2)>=2 and math.fabs(num3-num1)>=2):
        return True
    elif(math.fabs(num3-num2)==1 and math.fabs(num1-num2)>=2 and math.fabs(num3-num1)>=2):
        return True
    elif(math.fabs(num1-num3)==1 and math.fabs(num1-num2)>=2 and math.fabs(num2-num1)>=2):
        return True
    else:
        return False
    
print(close_number(5,6,7))
