def bracket(str):
    a=str.count("(")
    b=str.count(")")
    if(str.startswith(")") or str.endswith("(")):
        return False
    elif (a!=b):
        return False
    else:
        return True
string="()((())())"
print(bracket(string))
