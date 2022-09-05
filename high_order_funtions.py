#Estas son funciones que resiven a otras funciones como parametro, hay 3 principales, Filter, map y reduce

#filter; esta funcion recibe 2 parametros, la funcion y una lista para filtrar, además de eso simpre se encierra con la función "List", para transformar su retorno en una lista nueva. 

#map; En vez de usar un bucle for, la función map() proporciona una forma de "aplicar una función a cada elemento en un iterable", el primer valor va a ser la funcion que queremos aplicar, y el segundo valor va a ser la lista que queremos interar y aplicar la funcion



def filtrar():
    list_n = [1,4,5,234,62,3,123,1231,51,2]
    my_new_list= list(filter(lambda x: x%2 == 0, list_n))
    print(list_n)
    print(my_new_list)
    

def mapa():
    list_n=[1,2,3,4,5,6,7,8,9]
    map_funtion=list(map(lambda x: x**2, list_n))
    print(list_n)
    print(map_funtion)
    
def reducir():
    pass

if __name__=="__main__":
    filtrar()
    mapa()
    reducir()