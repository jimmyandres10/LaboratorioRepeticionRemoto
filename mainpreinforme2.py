def main():

    numero_de_notas = int(input("escriba el numero de notas que va a colocar "))
    cont_d = 0
    cant_n = 0
    for i in range(1,numero_de_notas+1):
        if  cont_d < numero_de_notas :
            nota = float(input("escriba su nota "))
            cant_n = nota + cant_n
            cont_d = cont_d + 1
            
    else:
            final_1 = (cant_n/numero_de_notas)
            print(f"esta es tu nota{final_1}")




if __name__ == "__main__":
    main()
