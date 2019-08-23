
print("escriba un numero para saber si es primo")
a = int(input("de un numero "))
contdep = 0
for i in range(1,a//2):
    if a % i == 0:
        contdep = contdep + 1



if contdep <= 1:
    print(f"su numero es primo {a}")
else:
    print(f"su numero no es primo {a}")    
