def main():
    #escribe tu código abajo de esta línea
    suma = 0
    cont = 0
    
    while(True):
        num = float(input())

        if num < 0:  #Número negativo
            break
        else:
            suma = suma + num
            cont += 1

    prom =  suma / cont
    print(prom)

if __name__=='__main__':
    main()

