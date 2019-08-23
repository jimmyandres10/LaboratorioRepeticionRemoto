

print("algoritmo que lea una cantidad variable de números y determine cuántos números fueron pares y cuántos impares. El algoritmo dejará de leer números cuando digite un número cero. ")
    
ndeveces = int(input("escriba la cantidad de numeros que va a dar "))
ndepares = 0
ndeimpares = 0


for i in range(1,ndeveces + 1 ):

        
    a = int(input("de su numero "))

    if a==0 :
        break
    else:
        if a % 2 == 0 :
            print(f"el numero {a} es par ")
            ndepares = ndepares + 1

        elif a % 2 != 0:
            print(f"el numero {a} es impar " )
            ndeimpares = ndeimpares + 1

