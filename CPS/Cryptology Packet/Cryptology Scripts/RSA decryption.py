import math
import extendedEuclideanAlg
def trialDivisionFactoring(pq):
    n = math.floor(math.sqrt(pq))
    isPrime = [1]*(n-1) # 0th position in isPrime correlates to the prime number 2
    for i in range(0 , n-1):
        if isPrime[i] == 0:
            continue
        if pq % (i+2) == 0:
            return [i+2, pq//(i+2)]
        for composite in range(i+i+2, n-1, i+2): # increment by the prime
            isPrime[composite] = 0

def polynomial(x, n, pq):
    return (x*x + n)%pq
def PollardRho(pq, n):
    print("Trying Pollard Rho with n =", n)
    x = 2
    y = x
    d = 1
    while d == 1: 
        x = polynomial(x, n, pq)
        y = polynomial(polynomial(y, n, pq), n, pq)
        d = math.gcd(abs(x-y), pq)
        # print(d)
    if d == n:
        return False
    return d

pq = int(input("pq: "))
E = int(input("E: "))
Me = int(input("M^e: "))

print("Using trial division:")
p, q = trialDivisionFactoring(pq)
privMod = (p-1)*(q-1)
D = extendedEuclideanAlg.extendedAlgorithm(E, privMod)['a'] if privMod < E else extendedEuclideanAlg.extendedAlgorithm(E, privMod)['b']
print("Decrypted message:", pow(Me, D, pq))

print("Using Pollard Rho:")
i = 1
temp = PollardRho(pq, i)
while temp == False:
    i+=1
    temp = PollardRho(pq)
p = temp
q = pq//p
print(p, q)
privMod = (p-1)*(q-1)
D = extendedEuclideanAlg.extendedAlgorithm(E, privMod)['a'] if privMod < E else extendedEuclideanAlg.extendedAlgorithm(E, privMod)['b']
print("Decrypted message:", pow(Me, D, pq))