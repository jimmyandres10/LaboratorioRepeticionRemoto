def main():

    import math

    print("escriba dos numeros, para calcular el cuadrado de uno y la raiz del otro")
    numero_b = float(input("Escriba un número : "))
    numero_d = float(input("Escriba un número : "))

    numero_c = math.sqrt(numero_d)

    print(f"el cuadrado del primer numero: {numero_b**2}")
    print(f"la raiz del segundo numero: {numero_c}")
   

if __name__ == "__main__":
    main()