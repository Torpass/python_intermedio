#Las list comprehensions es un manera simplificada de interar una lista y modificar sus valores solo si, si se cumplle una condicional, por ejemplo: (La condicional es opcional)
 
from pdb import post_mortem
from re import I


def list_comprehensions_names():

    first_name_list=["Pastor", "José"]
    last_name_list=["Jimenez","Lucena"]
    position= 0
    while position != 1:
        list_comprehensions= [interable.__add__(last_name_list[position]) for interable in first_name_list]
        position = position +1
        print(list_comprehensions) 
        return

    
#Acá podemos ver el uso de las condicionales, en una list comprehensions 

def list_comprehensions_numbers():
    list_numbers=[i**2 for i in range(1, 101) if i %3 == 0]
    print(list_numbers)
    return 

if __name__ == "__main__":
    list_comprehensions_names()
    list_comprehensions_numbers()

