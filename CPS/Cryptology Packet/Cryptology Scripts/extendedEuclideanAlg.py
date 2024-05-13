def euclideanGCD(a, b):
    equations = [] # list of dictionaries of form a = qb + r
    if(a < b):
        a, b = b, a
    r = -1
    while(r!=0):
        q = a // b
        r = a - q * b
        equations.append({'a':a, 'q':q, 'b':b, 'r':r}) 
        # print(str(a) + " = " + str(q) + "*" + str(b) + " + " + str(r))
        a, b = b, r
    # printDivisionEqs(equations)
    # print("gcd(" + str(equations[0]['a']) + ", " + str(equations[0]['b']) + ") = " + str(equations[-1]['b']))
    return equations

def printDivisionEqs(equations): 
    for eq in equations:
        print(str(eq['a']) + " = " + str(eq['q']) + "*" + str(eq['b']) + " + " + str(eq['r']))
def printExtendedEq(eq):
    print(str(eq['gcd']) + " = " + str(eq['a']) + "*" + str(eq['x']) + " + " + str(eq['b']) + "*" + str(eq['y'])) 

def extendedAlgorithm(a, b):
    equations = euclideanGCD(a, b)
    g = equations[-1]['b']
    if len(equations) < 2:
        printExtendedEq({'gcd':g, 'a':equations[0]['a'], 'x':0, 'b':equations[0]['b'], 'y':1})
        return {'gcd':g, 'a':equations[0]['a'], 'x':0, 'b':equations[0]['b'], 'y':1}
    equations=equations[-2::-1]
    a = 1
    x = equations[0]['a']
    b = -equations[0]['q']
    y = equations[0]['b']

    for i in range(1, len(equations)):
        # currEquation = {'gcd':g, 'a':a, 'x':x, 'b':b, 'y':y}
        # printExtendedEq(currEquation)

        newA = b
        newX = equations[i]['a']
        newB = a + b * -equations[i]['q']
        newY = x
        a, x, b, y = newA, newX, newB, newY
    currEquation = {'gcd':g, 'a':a, 'x':x, 'b':b, 'y':y}
    # printExtendedEq(currEquation)
    return currEquation
"""
extendedAlgorithm(2, 10) # testing when one number is the gcd of the other
print("="*20)
extendedAlgorithm(20, 97) # testing with example
print("="*20)
extendedAlgorithm(9876543210, 123456789) # a
print("="*20)
extendedAlgorithm(11111111111, 1000000001) # b 
print("="*20)
extendedAlgorithm(45666020043321, 73433510078091009) # c
"""