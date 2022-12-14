import random

def adivinaNumero():

    numero_pc = random.randint(1,10)
    vidas = 0
    jugando = True

    # Funcion para Solicitar numero al usuario y verificar si es valido
    def pedir_num():
        while True:
            num_elegido = 0
            numeros = [1,2,3,4,5,6,7,8,9,10]
            try:
                num_elegido = int(input("Ingresa la opcion: "))
            except ValueError:
                print("Debes escribir un número entre 1 y 10.")
                continue

            if num_elegido not in numeros:
                print("Debes escribir un número entre 1 y 10.")
                continue
            else:
                break

        return num_elegido
        
    print(" ")
    print("\t\tADIVINA UN NUMERO DEL 1 AL 10")
    print(" ")

    while jugando:      
            
            vidas += 1
            if vidas <= 3:
                num_elegido = pedir_num()   
                if int(num_elegido) == numero_pc:
                    print("\t\tHas acertado. Has necesitado", vidas, "vidas.")
                    jugando = False
                elif int(num_elegido) > numero_pc:
                    print("\t\tDemasiado alto. Llevas", vidas, "vidas.")
                elif int(num_elegido) < numero_pc:
                    print("\t\tDemasiado bajo. Llevas", vidas, "vidas.")

            else:
                print("\t\tSe te acabaron las vidas. Has perdido.")
                jugando = False 


    print(" ")
    jugar_de_nuevo = input("Quieres volver a Jugar ? (s/n): ")
    if jugar_de_nuevo == 's':
        adivinaNumero()
    else:
        print(" ")        
        print("\t\tPresiona enter para volver al menu...")
        k=input()