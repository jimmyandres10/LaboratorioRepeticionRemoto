
print("escriba un numero para saber si es primo")
a = int(input("de un numero "))
contdep = 0
i = 1
while i<=a//2 and contdep<=2:
    i=i+1
    if a % i == 0:
        contdep = contdep + 1


if contdep <= 1: 
    print(f"el numero es primo {a} ")
else:
    print(f"el numero no es primo {a} ")    
         

