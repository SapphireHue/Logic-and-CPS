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

pq = int(input("pq: "))
E = int(input("E: "))
Me = int(input("M^e: "))
p, q = trialDivisionFactoring(pq)
privMod = (p-1)*(q-1)
D = extendedEuclideanAlg.extendedAlgorithm(E, privMod)['a'] if privMod < E else extendedEuclideanAlg.extendedAlgorithm(E, privMod)['b']
print("Decrypted message:", pow(Me, D, pq))