def main():

    print("digite dos numeros los cuales quiera saber los numero naturales en medio de ellos respectivamente")
    n = int(input("escriba el primer numero  "))
    m = int(input("escriba el segundo numero  "))
    
    for i in range (n,m+1):
        if i>0:
            print(f"los numero son {i}")
        
    
    

if __name__ == "__main__":
    main()
