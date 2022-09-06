# Modos de Apertura

# r -> Solo lectura
# r+ -> Lectura y escritura
# w -> Solo escritura. Sobre escribe el archivo si existe. Crea el archivo si no existe
# w+ -> Escritura y lectura. Sobre escribe el archivo si existe. Crea el archivo si no existe
# a -> Añadido (agregar contenido). Crea el archivo si éste no existe
# a+ -> Añadido (agregar contenido) y lectura. Crea el archivo si éste no existe

# with open("./archivos/name.txt", "r", encoding="utf-8") as f:
# Acá usamos la funcion "open" que le pasaremos como parametro las ruta de nuestro archivo, y alguno del os metodos de escrituras antes vistos

#Todo el programa se basa principalmente en esta linea de codigo con diferentes metodos de entrada, sea r,r+, w, w+, a, a+ etc... 

def read():
    names = []
    with open("./archivos/name.txt", "r", encoding="utf-8") as f: 
        for line in f: 
            if len(line.strip()) > 0:
                names.append(line.strip())
    if len(names)> 0:
        print(names)
    else:
        print("Archivo vacio")

def write():
    names = []
    with open("./archivos/name.txt", "w" , encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write('\n')

def agregar_nombre(nombre):
    with open("./archivos/name.txt", "a" , encoding="utf-8") as f:
        f.write(nombre)
        f.write("\n")

def borrar_nombre(nombre):
    names = []
    with open("./archivos/name.txt", "r", encoding="utf-8") as f:
        for line in f: 
            if len(line.strip()) > 0 and line.strip()!= nombre:
                names.append(line.strip())
    with open("./archivos/name.txt", "w" , encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write('\n')

    
def run():
    sw = True
    while sw:
        try:
            print("""  
----------------------------------------------------------------------
            Seleccione un numero:
            1. Crear un nuevo archivo 
            2. Agregar nombre
            3. Listar nombre
            4. Borrar nombre
            5. Salir del programa
----------------------------------------------------------------------
            """)
            n = int(input("Ingrese una opcion :   "))
            if n == 1:
                write()
            elif n == 2:
                nombre = input("Ingrese el nombre a agregar: ")
                agregar_nombre(nombre)
            elif n == 3:
                read()
            elif n == 4:
                nombre = input("Ingrese el nombre a borrar : ")
                borrar_nombre(nombre)
            elif n ==5:
                sw = False
                print("Programa Terminado!")
        except ValueError :
                print("Error seleccione una opcion correcta")
    # write()

if __name__ == '__main__':
    run()