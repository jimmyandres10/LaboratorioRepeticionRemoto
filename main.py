def main():

#En donde se sabe que el discriminante d=√(b^2-4ac )
#tipo    ax2 + bx + c

    import math
    print("da valor a, da valor b, valor c, para hacer la operacion de ax2 + bx + c")

    letra_a = float(input("Escriba letra a: ")) 
    letra_b = float(input("Escriba letra b: "))
    letra_c = float(input("Escriba letra c: "))
    a = (letra_b**2)
    b = (4*(letra_a*letra_c))
    r = (a-b)
    d = math.sqrt(r)
    x1 = ((-letra_b) + math.sqrt(d))/(2*letra_a)
    x2 = ((-letra_b) - math.sqrt(d))/(2*letra_a)
    d2 = (-letra_b)/(2*letra_a)
    if d > 0:
        print(f"su respuesa en suma es {x1}")
        print(f"su respuesa en resta es {x2}")
        if d == 0:
            print(f"su respuesta es: {d2}" )
    else:
        print("no existe respuesta en numeros reales")
        
if __name__ == "__main__":
    main()