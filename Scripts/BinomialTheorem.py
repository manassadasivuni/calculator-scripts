factn = 1
factnr = 1
factr = 1
counter = 1

print("(A + Bx)^n")
A = int(input("A = "))
B = int(input("B = "))
n = int(input("n = "))

for r in range(n+1):

    while(counter <= n):
        factn = factn * counter
        counter += 1
                
    while(counter <= (n-r)):
        factnr = factnr * counter
        counter += 1
        
    while(counter <= r):
        factr = factr * counter
        counter += 1
        
    C = (factn / (factnr * factr)) * (A**(n-r)) * (B**r)

    print("x power " + str(r))
    print(C)
    