#En esta parte estaremos viendo como manjear exepciones en python con diversas funsiones

# TRY: En el try se coloca código que esperamos que pueda lanzar algún error.

# EXCEPT: En el except se maneja el error, es decir, si ocurre un error dentro del bloque de código del try, se deja de ejecutar el código del try y se ejecuta lo que se haya definido en el Except.

# ELSE: El else se ejecuta sólo si no hubo ninguna excepción lanzada desde el try

# FINALLY: Se ejecuta SIEMPRE, haya sido lanzada la excepción o no haya sido lanzada.

def divisors(num):
    divisors = [x for x in range(1, num+1) if num%x == 0]
    print(divisors)
    # for i in range(1, num + 1):
    #     if num % i == 0:
    #         divisors.append(i)
    # return divisors


def run():
    while True: #Ciclo while para ejecutar el programa hasta que se cumpla todo correctamente
        try:
            num = int(input('Ingresa un número: '))
            if num < 0:
                raise ValueError #En esta sentencia lanza un error cuando se percata que el numero ingresado por el usuario es menor a 0, es decir, un número negativo ó una cadena de texto, de ahí python manda un ValueError que es capturado por el exept. 
            print(divisors(num))
            print("Terminó mi programa")
            break
        #El value error es un sentencia que nos indica que a la función Divisiors se le ha agregado como argumento un string, cuando esto pasa, dispara el error, el exept retiene el error y ejecuta la linea abajo de el, en este caso un print
        except ValueError:
            print("Debes ingresar un entero positivo")


if __name__ == '__main__':
    run()