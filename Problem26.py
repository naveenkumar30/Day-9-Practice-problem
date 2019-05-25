#PF-Prac-26
def check_occurence(string):
    #start writing your code here
    string.lower()
    a=string.count("mat")
    b=string.count("jet")
    if(a==b):
        return True
    else:
        return False
        
string="mat jet Jet Mat"
print(check_occurence(string))
