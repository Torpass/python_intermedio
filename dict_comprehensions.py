#Es lo mismo que las listas compridas, solo que usaeremos diccionarios. Recuerda que los diccionarios tienen 2 valores para poder ser ubicados en el ciclo for, "la llave" y "el valor"
def run():
            #Aquí es donde se ve relflejado, la primera i representale la key y la segundo i representa el valor que se le va a asignar 
    my_dict= {i: i**3 for i in range(1,101) if i % 3 == 0}
    print(my_dict)


if __name__=="__main__":
    run()