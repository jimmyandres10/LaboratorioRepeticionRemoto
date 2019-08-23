def main():

    print("digite el numero donde termine la cadena")
    
    m = int(input("escriba el numero hasta donde quiere llegar  "))
    
    for i in range (1,m+1):
            t=((-1)**i)*i
            print(f"los numero son {t}")
        
    
    

if __name__ == "__main__":
    main()