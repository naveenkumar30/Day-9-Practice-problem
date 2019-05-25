#PF-Prac-8
def calculate_net_amount(trans_list):
    #start writing your code here
    p=0
    for i in trans_list:
        a=[]
        a=i.split(":")
        if(a[0]=='D'):
            p=p+int(a[1])
        else:
            p=p-int(a[1])
    
    return p

trans_list=["D:300","D:200","W:200","D:100"]
print(calculate_net_amount(trans_list))
