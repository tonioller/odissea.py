 
def xifrar(message, d):
    xifrat =""
    for letter in message:
        n = ord(letter)
        #print(F"v: {letter} ascii {n}")
        xifrat+=chr(n+d);
    return xifrat

message = "HolA odisseos!!!!"
print(xifrar(message, 1))
print(xifrar(message, 2))
print(xifrar(message, 3))

for i in range(1,10):
    print(str(i)+" "+xifrar(message, i))
