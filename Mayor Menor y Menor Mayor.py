print("Ingrese tres número enteros")
E=int(input("Elija 1 sí lo quiere de mayor a menor y 2 sí lo quiere de menor a mayor: "))
A=int(input("Digite un número: "))
B=int(input("Digite un número: "))
C=int(input("Digite un número: "))

if(E==1):
    if A>B and A>C:
        print(A)
        if B>C:
            print(B)
            print(C)
        else:
            print(C)
            print(B)

    elif B>A and B>C:
        print(B)
        if A>C:
            print(A)
            print(C)
        else:
            print(C)
            print(A)

    elif C>A and C>B:
        print(C)
        if A>B:
            print(A)
            print(B)
        else:
            print(B)
            print(A)

if(E==2):
    if A<B and A<C:
        print(A)
        if B<C:
            print(B)
            print(C)
        else:
            print(C)
            print(B)

    elif B<A and B<C:
        print(B)
        if A<C:
            print(A)
            print(C)
        else:
            print(C)
            print(A)

    elif C<A and C<B:
        print(C)
        if A<B:
            print(A)
            print(B)
        else:
            print(B)
            print(A)


        




        
