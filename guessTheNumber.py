import random

#random.seed(6)

theNumber=random.randint(1, 100);


end = False;

while not(end) :
    print("Quin número creus que és?. En cas de voler abandonar escriu -1");
    n = int(input());
        
    if (n<0) :
        print("Gràcies per participar. Fins aviat");
        end = True;
    elif (n < theNumber):
        print("El nombre que cerques és més gran");
    elif (n > theNumber):
        print("El nombre que cerques és més petit");
    elif (n == theNumber):
        print(F"Ho has encertat era el {theNumber}!!")
        end = True;
    
