def Sum(*p):
    c = 0
    for i in p:
        c+=i
    return c

def Product(*p):
    c = 1
    for i in p:
        c*=i
    return c