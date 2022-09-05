DATA = [
    {
        'name': 'Facundo',
        'age': 32,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def all_position(Datas):
    works=['Language Maker', 'Human Resources Manager', 'Student', 'Support', 'Backend Developer','Associate', 'QA Manager','UX Designer','Technical Coach']

    selection=int(input('Seleccione el trabajo que busca:\n1)Language Maker\n2)Human Resources Manager\n3)Student\n4)Support\n5)Backend Developer\n6)Associate\n7)QA Manager\n8)UX Designer\n9)Technical Coach\n: '))
    selection_ = works[selection-1]
    all_workers=[worker['name'] for worker in Datas if worker['position']==selection_]
    print(all_workers)


def all_languages(Datas):   
    languages=['python','go','java','javascript','ruby']
    selection=int(input('Seleccione el lenguaje:\n1)python\n2)go\n3)java\njavascript\n5)ruby\n:')) 
    selection_=languages[selection-1]
    print(selection_)

    all_language=[worker['name'] for worker in Datas if worker['language']==selection_]
    print(all_language)


def all_companies(Datas):
        companies=['Python Organization','Master','Rappi','Platzi','Everis','Globant']
        selection=int(input('Seleccione la organizacion:\n1)Python Organization\n2)Master\n3)Rappi\n4)Platzi\n5)Everis\n6)Globant\n:'))
        selection_=companies[selection-1]
        all_busnises=[worker['name'] for worker in Datas if worker['organization'] == selection_]
        print(all_busnises)


def run():

    selection=int(input('Seleccione que desea ver:\n1)Cargo correspondiente a cada empleado\n2)Tecnología que usa cada empleado\n3)Compañía en que que trabaja cada empleado\n:'))
    if selection == 1:
        all_position(DATA)
    elif selection == 2:
        all_languages(DATA)
    elif selection == 3:
        all_companies(DATA)
    else:
        print('Seleccion incorrecta ingrese de nuevo')
    
    print('Programa finalizado')
    

if __name__=='__main__':
    run()