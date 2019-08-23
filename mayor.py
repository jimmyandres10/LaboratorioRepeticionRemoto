def main():
    
    print("escriba 10 numeros para definir cuantos son positivos, negativos y ceros")
    
    npositivo = 0
    nnegativo = 0
    ncero = 0
    
    
    for i in range (1,11):

        a = int(input(f"digite el {i} numero "))
    
        if a > 0 :
            print(f"el numero {a} es mayor a 0")
            npositivo = npositivo + 1
    
        elif a < 0:
            print(f"el numero {a} es menor a 0")
            nnegativo = nnegativo + 1

        else:
            print(f"el numero {a} es 0")
            ncero = ncero + 1

    print(f"La cantidad de numero positivos fue {npositivo}, la cantidad de numeros negativos fue {nnegativo}, la cantidad de 0 es {ncero}")

if __name__ == "__main__":
    main()