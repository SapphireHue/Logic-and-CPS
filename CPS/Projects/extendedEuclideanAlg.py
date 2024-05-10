def euclideanGCD(a, b):
    equations = [] # list of dictionaries of form a = qb + r
    if(a < b):
        a, b = b, a
    r = -1
    while(r!=0):
        q = a // b
        r = a - q * b
        equations.append({'a':a, 'q':q, 'b':b, 'r':r}) 
        a, b = b, r
    return equations

def solve(origA, origB, c):
    equations = euclideanGCD(origA, origB)
    g = equations[-1]['b']
    a = x = b = y = 0
    if c%g != 0:
        return "no solution"
    if len(equations) < 2:
        a = equations[0]['a']
        x = 0
        b = equations[0]['b']
        y = 1
    else:
        equations=equations[-2::-1]
        a = equations[0]['a']
        x = 1
        b = equations[0]['b']
        y = -equations[0]['q']

        for i in range(1, len(equations)):
            newA = equations[i]['a']
            newX = y
            newB = a
            newY = x + y * -equations[i]['q']
            a, x, b, y = newA, newX, newB, newY
    if(a != origA):
        a, x, b, y = b, y, a, x 
    factor = c//g
    return str(c) + " = " + str(a) + "*" + str(x*factor) + " + " + str(b) + "*" + str(y*factor)