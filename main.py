def main():

    import math
    print("escriba dos numeros, para calcular el cuadrado del primero y el doble, la suma de los dos y la raiz del segundo")
    numero_b = float(input("Escriba un número : ")) 
    numero_d = float(input("Escriba un número : "))

    numero_s = numero_b + numero_d
    numero_c = math.sqrt(numero_d)

    print(f"el cuadrado del primer numero: {numero_b**2}")
    print(f"la raiz del segundo numero: {numero_c}")
    print(f"la suma de esos dos numeros: {numero_s}")
    print(f"el doble del primer numero: {numero_b*2}")

if __name__ == "__main__":
    main()