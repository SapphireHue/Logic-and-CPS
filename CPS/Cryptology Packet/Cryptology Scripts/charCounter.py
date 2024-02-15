alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
frequencies = {}
for letter in alphabet:
    frequencies[letter] = 0

message = input("Message: ")
for letter in message:
    if letter in frequencies:
        frequencies[letter]+=1
print(frequencies)
