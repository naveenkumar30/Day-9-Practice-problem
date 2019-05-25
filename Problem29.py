def exchange_list(number_list):
    #start writing your code here
    a=[]
    b=[]
    for i in range(0,len(number_list)):
        if(i<len(number_list)/2):
            a.append(number_list[i])
        else:
            b.append(number_list[i])
    b.reverse()
    
    number_list.clear()
    number_list=b+a
    return number_list
number_list=[1,2,3,4,5,6,7,8,9,10]
print(exchange_list(number_list))
