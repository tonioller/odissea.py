1. AREA I
=========

PI = 3.14
r = 5
area = PI * r * r
print("Area of a circle = %.2f" %area)

2. AREA II
==========

r = 5
area = r * r
print("Area of a square = %.2f" %area)


3. AREA III
=======
def areaSquare(r):
   return r*r


print(str(areaSquare(5)))   
print(str(areaSquare(10)))  

print(areaSquare(5)) 


4. Factorial!!!
============

n = 5
fact = 1
for i in range(1,n+1):
   fact = fact * i
   print(i," : ", fact)


def factorial(n):
   fact = 1
   for i in range(1,n+1):
      fact = fact * i 
   return fact

print(factorial(3))


===========================================
5.- CEASER!!!!!


def encrypt(text,s):
   result = ""
   # transverse the plain text
   print(len(text))
   for i in range(len(text)):
      char = text[i]
      print("iteració " + str(i)+" "+char)
      # Encrypt uppercase characters in plain text
      
      if (char.isupper()):
         result += chr((ord(char) + s-65) % 26 + 65)
      # Encrypt lowercase characters in plain text
      else:
         result += chr((ord(char) + s - 97) % 26 + 97)
      print("result "+result)   
   return result

#check the above function
text = "CEASER CIPHER DEMO"
#GIWEVIBEQTPIIWX
s = 4

print ("Plain Text : " + text)
print ("Shift pattern : " + str(s))
print ("Cipher: " + encrypt(text,s))

==============


6.-
message = 'GIEWIVrGMTLIVrHIQS' #encrypted message


def decrypt(message):
   LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
   for key in range(len(LETTERS)):
      translated = ''
      for symbol in message:
         if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key
            if num < 0:
               num = num + len(LETTERS)
            translated = translated + LETTERS[num]
         else:
            translated = translated + symbol
      print('Hacking key #%s: %s' % (key, translated))
      
decrypt(message)

