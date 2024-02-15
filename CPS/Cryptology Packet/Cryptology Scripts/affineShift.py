alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def multiplicativeInverse(num):
    for i in range(1, 26):
        if (num*i)%26 == 1:
            return i

def encrypt(message, a, b):
    out = ""
    for letter in message:
        if letter in alphabet:
            out += alphabet[(a*(alphabet.find(letter))+b)%26]
        else:
            out+=letter
    return out

def decrypt(message, a, b):
    out = ""
    aInverse = multiplicativeInverse(a)
    for letter in message:
        if letter in alphabet:
            out += alphabet[((alphabet.find(letter) - b) * aInverse)%26]
        else:
            out+=letter
    return out

def freqCount(message):
    frequencies = {}
    for letter in alphabet:
        frequencies[letter] = 0

    for letter in message:
        if letter in frequencies:
            frequencies[letter]+=1
    return frequencies

message = input("What is your message?")
a = input("Value of a (leave blank for 1): ")
a = 1 if len(a)==0 else int(a)
b = input("Value of b (leave blank for 0): ")
b = 0 if len(b)==0 else int(b)
print("Encrypted: " + encrypt(message, a, b))
print("Decrypted: " + decrypt(message, a, b))