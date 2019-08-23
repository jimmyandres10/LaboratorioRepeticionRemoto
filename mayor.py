def main():

    print("escriba un numero para saber si es mayor que 0 ")
    a = int(input("digite el valor de a "))

    if a > 0 :
        print("el numero es mayor a 0")
    
    elif a == 0:
        print("el numero es igual a 0")

    else:
        print("el numero es menor a 0")



if __name__ == "__main__":
    main()