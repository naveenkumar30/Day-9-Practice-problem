def bracket(str):
    a=str.count("(")
    b=str.count(")")
    if(str.startswith(")") or str.endswith("(")):
        return False
    elif (a==b):
        return True
    else:
        return False
string="()((())())"
print(bracket(string))
