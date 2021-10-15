def main():
    num = int(input("Enter a number: "))
    #escribe tu código abajo de esta línea
    inv=str(num)
    cont=len(inv)
    if cont<=6:
        if num < 0:
            numero= num*-1
            n=int(str(numero)[::-1])
            m=n*-1
            print(m)
        else:
            n=int(inv[::-1])
            print(n)
    else:
        print('Too long')    


if __name__=='__main__':
    main()
