#Las lambda funtions son funciones "Invisibles" por así decirlo, solo puede ocupar una línea de código y el resultado retonar directamente en la variable. En este caso, vemos que retorna el valor true o el valor false

#La estructura es sencilla, se inicia una variable x, posteriormente se le asigna los argumentos como variables internas de la funcion y al final se le da la instruccion

#Para invocar una funcion lambda se debe llamar a la variable asignada y ingresar los argumentos en parentesis

def run():
    text=input("Ingrese una plaabra: ")
    palindrome= lambda variable: variable==variable[::-1]
    print(palindrome(text))

    if palindrome == True: 
        print("Si sirve")


if __name__=="__main__":
    run()