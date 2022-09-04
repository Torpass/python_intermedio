def run():
    my_list=[1, "hello", True, 4.5]
    my_dict={"first_name": "Torpas", "last_name": "Jimenez"}

    super_list= [
        {"first_name": "German", "last_name": "Rosales"},
        {"first_name": "Pastor", "last_name": "José"},
        {"first_name": "Abraham", "last_name": "Hernández"},
        {"first_name": "Luis", "last_name": "Herice"},
    ]

    super_dict={
        "1" : [1,2,3,4],
        "2" : [5,6,7,8],
        "3" : [9,10,11,12],
        "4" : [13,14,15,16],
    }

# tenemos un ciclo for con la variable values que agarra todos los diccionarios de la lista, posteriormente un ciclo for aninado recorre los diccionarios de values con sus 2 variables "key" y "value". El .items es un método que nos permite tranformar el diciconario para que se pueda recorrer
 
    for values in super_list:
        for key, value in values.items():
            print(f'{key} - {value}')

    for key, value in super_dict.items():
        print(f"La key del diccionario {key}\n contiene estos valores: {value}")

if __name__== "__main__":
    run()